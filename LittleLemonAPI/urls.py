from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from LittleLemonAPI.views import MenuItemsView, SingleMenuItemView, msg

urlpatterns = [
    path('menu-items/', MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', ObtainAuthToken.as_view()),
    path('message/', msg),
]