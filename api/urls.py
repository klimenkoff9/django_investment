from django.urls import path
from .views import StoreView, CreateStoreView, PlaceOrder

urlpatterns = [
    path('login', StoreView.as_view()),
    path('create', CreateStoreView.as_view()),
    path('get', PlaceOrder.as_view())
]
