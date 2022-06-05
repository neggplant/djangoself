from django.urls import path

from . import views

urlpatterns = [
    path('', views.health, name='health'),
    path('health1', views.health1, name='health1'),
    path('async_sleep/', views.AsyncSleep.as_view()),
    path('sleep', views.sleep_view),
]