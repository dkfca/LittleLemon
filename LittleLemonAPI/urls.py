from django.urls import path
from LittleLemonAPI.views import home, MenuItemsView, SingleMenuItemView, BookingsView, SingleBookingView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', home, name='home'),
    path('booking/', BookingsView.as_view()),
    path('booking/<int:pk>', SingleBookingView.as_view()),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
