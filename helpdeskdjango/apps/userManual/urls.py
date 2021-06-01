from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.userManualView.as_view()),
]
