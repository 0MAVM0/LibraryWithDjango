from django.urls import path
from .views import *

urlpatterns = [
    path("", home_page, name="home"),
    path("detail/<int:id>/", detail_page, name="detail_page"),
]
