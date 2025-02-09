from django.urls import path

from . import views
from django.urls import path

app_name = "quotes"
urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('author_detail/<int:author_id>', views.author_detail, name='author_detail'),
    path('add_tag', views.add_tag, name='add_tag'),
    path('add_author', views.add_author, name='add_author'),
    path('add_quote', views.add_quote, name='add_quote'),
]

