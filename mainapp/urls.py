from django.urls import path
from .views import page_in_process, main_page, profile_page, book_like, test


app_name = "mainapp"


urlpatterns = [
    path("", main_page, name="copleated_book"),
    path("process/", page_in_process, name="process_books"),
    path("profile/", profile_page, name="profile"),
    path("like/", book_like, name="like"),
    path("test/", test, name="test"),
]
