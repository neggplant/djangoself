from django.urls import path

from . import views

urlpatterns = [
    path('health/', views.QustionChoiceView.as_view(), name='QustionChoiceView'),
]