from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/search', views.search_view, name='search_view'),
    path('restaurant/<int:pk>/', views.restaurant_detail, name='restaurant_detail')
]
