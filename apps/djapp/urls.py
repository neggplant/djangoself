from django.urls import path

from . import views

urlpatterns = [
    path('health/', views.HealthView.as_view(), name='HealthView'),
    path('aggregate/', views.AggregateView.as_view(), name='AggregateView'),
    path('redirect/', views.RedirectView.as_view(), name='RedirectView'),
    path('sendemail/', views.SendEmailView.as_view(), name='SendEmailView'),
]
