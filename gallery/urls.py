from django.urls import path
from . import views

urlpatterns = [
    path('', views.GalleryView.as_view(), name='gallery'),
    path('collection/<slug:slug>/', views.CollectionView.as_view(), name='collection'),
]
