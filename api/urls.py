from django.urls import path
from . import views
from django.conf.urls import url
from api.views import UserRegistrationView

urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view(), name='signup_view'),
    
]