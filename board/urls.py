from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
  path('list/', views.List.as_view(), name='list'),
  path('create/', views.Create.as_view(), name='create'),
  path('<int:pk>/', views.Detail.as_view(), name='detail'),
  path('update/<int:pk>', views.Update.as_view(), name='update'),
  path('delete/<int:pk>', views.Delete, name='delete'),
]