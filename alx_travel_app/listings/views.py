from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all bookings
        for the currently authenticated user.
        """
        user = self.request.user
        return Booking.objects.filter(user=user)
