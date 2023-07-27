from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
from mainapp.models import Users_books
import os
from django.db.models import F

# Create your views here.


def main_page(request):
    if request.method == "POST":
        if request.POST.get('book_id'):
            Users_books.objects.filter(pk=request.POST['book_id']).delete()
            os.remove(os.path.join(settings.MEDIA_ROOT, request.POST['delete_book_image']))
            return HttpResponseRedirect(reverse('copleated_book'))
        else:
            book = Users_books(owner=request.user,
                        book_name=request.POST["book_name"],
                        author_name=request.POST["author_name"],
                        year_of_writing=request.POST["year_of_writing"],
                        total_page=request.POST["total_page"],
                        current_page=request.POST["current_page"],
                        description=request.POST["description"],
                        book_image=request.FILES['book_image'])
            book.save()
            return HttpResponseRedirect(reverse('copleated_book'))

    else:
        if request.user.is_authenticated:
            result = Users_books.objects.filter(owner=request.user, current_page__gte=F('total_page'))
            books = len(result)
            pages = sum((x.total_page for x in result))
            content = {"result": result, "books": books, "pages": pages}
            return render(request, 'mainapp/compleated_page.html', content)
        return render(request, 'mainapp/compleated_page.html')


def page_in_process(request):
    if request.method == "POST":
        if request.POST.get('book_id'):
            Users_books.objects.filter(pk=request.POST['book_id']).update(current_page=request.POST['update_current_page'])
            return HttpResponseRedirect(reverse('process_books'))
        else:
            book = Users_books(owner=request.user,
                        book_name=request.POST["book_name"],
                        author_name=request.POST["author_name"],
                        year_of_writing=request.POST["year_of_writing"],
                        total_page=request.POST["total_page"],
                        current_page=request.POST["current_page"],
                        description=request.POST["description"],
                        book_image=request.FILES['book_image'])
            book.save()
            return HttpResponseRedirect(reverse('process_books'))

    if request.user.is_authenticated:
            result = Users_books.objects.filter(owner=request.user, current_page__lt=F('total_page'))
            books = len(result)
            pages = sum((x.total_page for x in result))
            content = {"result": result, "books": books, "pages": pages}
            return render(request, 'mainapp/process_page.html', content)



def profile_page(request):
    result = Users_books.objects.filter(owner=request.user, current_page__gte=F('total_page'))
    content = {'books': len(result)}
    return render(request, 'mainapp/profile_page.html', content)
