from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/submit/', views.contact_submit_view, name='contact_submit'),
]
