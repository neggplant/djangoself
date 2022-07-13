from django.urls import path

from . import views

urlpatterns = [
    path('health/', views.QustionChoiceView.as_view(), name='QustionChoiceView'),
    path('aggregate/', views.AggregateView.as_view(), name='AggregateView'),
    path('redirect/', views.RedirectView.as_view(), name='RedirectView'),
]