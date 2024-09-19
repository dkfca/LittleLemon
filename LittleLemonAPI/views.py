from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from LittleLemonAPI.models import Menu, Booking
from LittleLemonAPI.serializers import MenuSerializer, BookingSerializer

def home(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookingView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = BookingSerializer

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer