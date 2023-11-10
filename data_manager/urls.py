from django.urls import path
from . import views

urlpatterns = [
    path('api/servers/', views.ServerList.as_view()),
    path('servers/<str:pk>/', views.ServerDetail.as_view()),
    path('servers/metrics/<str:pk>/', views.MetricList.as_view()),
    path('servers/<int:pk>/metrics/<int:metric_pk>/', views.MetricDetail.as_view()),

    path('server/<str:pk>/invite/', views.InviteView.as_view()),

]