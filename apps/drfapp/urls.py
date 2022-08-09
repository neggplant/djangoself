from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('health/', views.HealthView.as_view()),
    path('snippets/aggregate/', views.SnippetAggregate.as_view()),
    path('snippets/', views.Snippets.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# from rest_framework import routers
#
# router = routers.SimpleRouter()
# router.register(r'health/', views.HealthView, basename='drf_health')
# router.register(r'snippets/aggregate/', views.SnippetAggregate)
# router.register(r'snippets/<int:pk>/', views.SnippetDetail)
# urlpatterns = format_suffix_patterns(router.urls)
