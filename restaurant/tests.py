from django.test import TestCase
from .models import Menu, Booking
from django.urls import reverse

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="Ice Cream", price=80.00, description="Test description")
        self.assertEqual(str(item), "Ice Cream")

class BookingTest(TestCase):
    def test_booking_creation(self):
        booking = Booking.objects.create(first_name="John Doe", reservation_date="2026-05-28", reservation_slot=12)
        self.assertEqual(str(booking), "John Doe - 2026-05-28 (Slot: 12)")

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(name="Greek Salad", price=12.99, description="Greek salad")
        self.item2 = Menu.objects.create(name="Lemon Dessert", price=5.00, description="Lemon dessert")

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item1.name)
        self.assertContains(response, self.item2.name)

class BookingViewTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(first_name="Jane Doe", reservation_date="2026-05-28", reservation_slot=15)

    def test_bookings_list_api(self):
        response = self.client.get(reverse('bookings') + '?date=2026-05-28')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf-8'),
            [{'first_name': 'Jane Doe', 'reservation_slot': 15}]
        )
