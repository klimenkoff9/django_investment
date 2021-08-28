from django.urls import path
from .views import StoreView, CreateStoreView, PlaceOrder

urlpatterns = [
    path('view', StoreView.as_view()),
    path('add-key', CreateStoreView.as_view()),
    path('place-order', PlaceOrder.as_view())
]
