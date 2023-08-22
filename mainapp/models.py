from django.conf import settings
from django.db import models

# Create your models here.


class Users_books(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="books"
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="liked_images"
    )
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    year_of_writing = models.PositiveIntegerField()
    total_page = models.IntegerField()
    current_page = models.IntegerField()
    description = models.TextField()
    book_image = models.ImageField(upload_to="images/")
