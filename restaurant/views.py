from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import Menu, Booking
from .forms import BookingForm
from datetime import datetime

def home(request):
    specials = Menu.objects.all()[:3]
    return render(request, 'restaurant/index.html', {'specials': specials})

def about(request):
    return render(request, 'restaurant/about.html')

def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'restaurant/menu.html', {'menu_items': menu_items})

def menu_item(request, pk):
    item = get_object_or_404(Menu, pk=pk)
    return render(request, 'restaurant/menu_item.html', {'menu_item': item})

@login_required(login_url='login')
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data['reservation_date']
            reservation_slot = form.cleaned_data['reservation_slot']
            exists = Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot).exists()
            if exists:
                form.add_error('reservation_slot', 'This slot is already booked for the selected date.')
            else:
                form.save()
                return redirect('book')
    
    today = datetime.today().strftime('%Y-%m-%d')
    bookings = Booking.objects.filter(reservation_date=today)
    return render(request, 'restaurant/book.html', {'form': form, 'bookings': bookings, 'today': today})

def bookings(request):
    date = request.GET.get('date', datetime.today().strftime('%Y-%m-%d'))
    bookings_on_date = Booking.objects.filter(reservation_date=date)
    data = []
    for b in bookings_on_date:
        data.append({
            'first_name': b.first_name,
            'reservation_slot': b.reservation_slot
        })
    return JsonResponse(data, safe=False)

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'restaurant/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'restaurant/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
