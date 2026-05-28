from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Little Lemon! (Step 1)")

def about(request):
    return HttpResponse("About Little Lemon")

def book(request):
    return HttpResponse("Book a table")

def menu(request):
    return HttpResponse("Menu")

def menu_item(request, pk=None):
    return HttpResponse(f"Menu Item {pk}")

def bookings(request):
    return HttpResponse("Bookings List")

def signup_view(request):
    return HttpResponse("Signup")

def login_view(request):
    return HttpResponse("Login")

def logout_view(request):
    return HttpResponse("Logout")

