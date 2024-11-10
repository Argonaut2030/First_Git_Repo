from django.urls import path

from . import views
from django.urls import path, include

app_name = "quotes"
urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('users/', include('users.urls'))
]

