from django.contrib import admin
from django.urls import path
from app.views import order_total_view, hey_you_view, age_in_view

urlpatterns = [
    path("order-total/<burgers>/<fries>/<drinks>", order_total_view),
    path("age-in/<int:end>/<int:birth>", age_in_view),
    path("hey/<name>", hey_you_view),
    path("admin/", admin.site.urls),
]
