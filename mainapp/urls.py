from django.urls import path
from .views import main_page, profile_page


app_name = "mainapp"


urlpatterns = [
    path("", main_page, name="copleated_book"),
    path("profile/", profile_page, name="profile"),
]
