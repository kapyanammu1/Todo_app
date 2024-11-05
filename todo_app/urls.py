from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_view, name='todo'),
    path('delete_item/<int:pk>/', views.Delete_item, name='delete_item'),
    path('update_item/<int:pk>/', views.update_todo_complete, name='update_item'),
]