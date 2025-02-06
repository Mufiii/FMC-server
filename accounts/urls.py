from django.urls import path
from accounts.views import UserRegistrationAPIView

urlpatterns = [
    path('register/',UserRegistrationAPIView.as_view(),name='register')
]
