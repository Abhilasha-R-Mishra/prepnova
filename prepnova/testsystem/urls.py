from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-test/', views.create_test, name='create_test'),
    path('test/<int:test_id>/', views.attempt_test, name='attempt_test'),
    path('result/<int:test_id>/', views.result_view, name='result'),
    path('ai-interview/', views.ai_interview, name='ai_interview'),
    path('ai-response/', views.ai_response, name='ai_response'),
]
