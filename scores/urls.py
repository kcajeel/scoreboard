from django.urls import path

from . import views

app_name = "scores"
urlpatterns = [
    # ex: /
    path("", views.index, name="index"),
    # ex: /5/
    path("<int:id>/", views.detail, name="detail"),
]