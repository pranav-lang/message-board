from django.urls import URLPattern, path
from .views import HomePageView

urlpatterns = [
    path('',HomePageView.as_view(),name = 'home'),
]
