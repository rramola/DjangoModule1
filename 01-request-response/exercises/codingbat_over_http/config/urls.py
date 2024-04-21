from django.contrib import admin
from django.urls import path
# from app.views import (
#     warmup_one_view,
#     warmup_two_view,
#     warmup_three_view,
#     warmup_four_view,
# )

import app.views

urlpatterns = [
    # path("warmup-four/<int:num1>/<int:num2>/<int:num3>", warmup_four_view),
    # path("warmup-three/<word>", warmup_three_view),
    # path("warmup-two/<word>", warmup_two_view),
    # path("warmup-one/<int:num>", warmup_one_view)
    path("challenges/", app.views.challenges, name="challenges"),
    path("admin/", admin.site.urls),
]
