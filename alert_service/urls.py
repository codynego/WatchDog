from django.urls import path
from . import views

urlpatterns = [
    path('server/alerts/', views.AlertAPIView.as_view()),
]