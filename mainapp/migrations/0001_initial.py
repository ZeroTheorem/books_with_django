# Generated by Django 3.2.20 on 2023-07-24 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.TextField()),
                ('author_name', models.TextField()),
                ('year_of_writing', models.PositiveIntegerField()),
                ('total_page', models.PositiveIntegerField()),
                ('current_page', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('book_image', models.ImageField(upload_to='static/images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
