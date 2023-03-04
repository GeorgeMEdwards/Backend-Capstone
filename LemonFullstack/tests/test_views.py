from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.utils import timezone
import json

from restaurant.models import Booking
from restaurant.serializers import BookingSerializer

class BookingViewSetTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

        self.booking1 = Booking.objects.create(
            first_name = 'Ali Baba',
            reservation_slot = 2,
            reservation_date = timezone.now()
        )
        self.booking2 = Booking.objects.create(
            first_name = 'John Wayne',
            reservation_slot = 6,
            reservation_date = timezone.now()
        )
        self.valid_payload = {
            'first_name': 'Test Booking',
            'reservation_slot': 3,
            'reservation_date': timezone.now()
        }
        self.invalid_payload = {
            'first_name': '',
            'reservation_slot': '',
            'reservation_date': ''
        }

    def test_get_all_bookings(self):
        response = self.client.get(reverse('booking-list'))
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_booking(self) -> None:
        response = self.client.post(
            reverse('booking-list'),
            data = json.dumps(self.invalid_payload, cls=DjangoJSONEncoder),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_valid_single_booking(self) -> None:
        response = self.client.get(reverse('booking-detail', kwargs={'pk': self.booking1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        booking = Booking.objects.get(pk=self.booking1.pk)
        serializer = BookingSerializer(booking)
        self.assertEqual(response.data, serializer.data)
        
        