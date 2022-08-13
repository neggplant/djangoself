from django.urls import path

from . import views

urlpatterns = [
    path('async_sleep/', views.AsyncSleep.as_view()),
    path('exc/', views.exc_view),
    path('health/', views.health, name='basehealth'),
    path('send_rabbitmq/', views.RabbitMQView.as_view()),
    path('send_rabbitmq_thread/', views.RabbitMQThreadView.as_view()),
    path('sleep/', views.sleep_view),
    path('signal/', views.signal_view),
]
