from django.db import models
from authnapp.models import my_User
# Create your models here.


class Users_books(models.Model):

    owner = models.ForeignKey(my_User, on_delete=models.CASCADE)
    book_name = models.TextField()
    author_name = models.TextField()
    year_of_writing = models.PositiveIntegerField()
    total_page = models.PositiveIntegerField()
    current_page = models.PositiveIntegerField()
    description = models.TextField()
    book_image = models.ImageField(upload_to='images/')
