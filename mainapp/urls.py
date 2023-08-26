from django.urls import path
from .views import get_all_book, create_or_delete_book, profile_page, users_list, follow


app_name = "mainapp"


urlpatterns = [
    path("", get_all_book, name="copleated_book"),
    path("create_or_delete_book/", create_or_delete_book, name="create_or_delete_book"),
    path("profile/", profile_page, name="profile"),
    path("users-list/", users_list, name="users_list"),
    path("follow/", follow, name="follow"),
]
