from django.urls import path
from .views import LoginAPIView, SendEmailAPIView
#from notification.views import LoginAPIView, SendAPIView

urlpatterns = [
    path('auth/login/', LoginAPIView.as_view(), name='login'),
    path('send/', SendEmailAPIView.as_view(), name='send_email'),
]