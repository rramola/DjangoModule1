from django.contrib import admin
from django.urls import path
from app.views import (
    warmup_one_view,
    warmup_two_view,
    warmup_three_view,
    warmup_four_view,
)


urlpatterns = [
    path("warmup-four-view", warmup_four_view),
    path("warmup-three/<word>", warmup_three_view),
    path("warmup-two/<word>", warmup_two_view),
    path("warmup-one/<int:num>", warmup_one_view),
    path("admin/", admin.site.urls),
]
