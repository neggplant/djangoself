from django.urls import path

from . import views

urlpatterns = [
    path('health/', views.health, name='health1'),
    path('async_sleep/', views.AsyncSleep.as_view()),
    path('sleep/', views.sleep_view),
]