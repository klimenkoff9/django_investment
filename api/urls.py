from django.urls import path
from .views import KeysView, AddKeyView, OrderView, OrdersView

urlpatterns = [
    path('view', KeysView.as_view()),
    path('add-key', AddKeyView.as_view()),
    path('place-order', OrderView.as_view()),
    path('view-orders', OrdersView.as_view()),
]
