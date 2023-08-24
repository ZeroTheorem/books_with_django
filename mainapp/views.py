from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.http import HttpResponseRedirect
from mainapp.models import Users_books
from django.http import JsonResponse
import os
from django.db.models import F
from time import sleep
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


@login_required
def main_page(request):
    if request.method == "POST":
        if request.POST.get("book_id"):
            Users_books.objects.filter(pk=request.POST["book_id"]).delete()
            os.remove(
                os.path.join(settings.MEDIA_ROOT, request.POST["delete_book_image"])
            )
            return HttpResponseRedirect(reverse("mainapp:copleated_book"))
        else:
            book = Users_books(
                owner=request.user,
                book_name=request.POST["book_name"],
                author_name=request.POST["author_name"],
                year_of_writing=request.POST["year_of_writing"],
                total_page=request.POST["total_page"],
                current_page=request.POST["current_page"],
                description=request.POST["description"],
                book_image=request.FILES["book_image"],
            )
            book.save()
            return HttpResponseRedirect(reverse("mainapp:copleated_book"))

    else:
        result = Users_books.objects.filter(
            owner=request.user, current_page__gte=F("total_page")
        )
        books = len(result)
        pages = sum((x.total_page for x in result))
        paginator = Paginator(result, 10)
        page_number = request.GET.get("page", 1)
        try:
            page = paginator.page(page_number)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            page = paginator.page(1)

        content = {"page": page, "books": books, "pages": pages}
        return render(request, "mainapp/compleated_page.html", content)


@login_required
def page_in_process(request):
    if request.method == "POST":
        if request.POST.get("book_id"):
            Users_books.objects.filter(pk=request.POST["book_id"]).update(
                current_page=request.POST["update_current_page"]
            )
            return HttpResponseRedirect(reverse("mainapp:process_books"))
        else:
            book = Users_books(
                owner=request.user,
                book_name=request.POST["book_name"],
                author_name=request.POST["author_name"],
                year_of_writing=request.POST["year_of_writing"],
                total_page=request.POST["total_page"],
                current_page=request.POST["current_page"],
                description=request.POST["description"],
                book_image=request.FILES["book_image"],
            )
            book.save()

            return HttpResponseRedirect(reverse("mainapp:process_books"))

    else:
        result = Users_books.objects.filter(
            owner=request.user, current_page__lt=F("total_page")
        )
        books = len(result)
        pages = sum((x.total_page for x in result))
        content = {"result": result, "books": books, "pages": pages}
        return render(request, "mainapp/process_page.html", content)


def profile_page(request):
    result = Users_books.objects.filter(
        owner=request.user, current_page__gte=F("total_page")
    )
    pages = sum((x.total_page for x in result))
    content = {"books": len(result), "pages": pages}
    return render(request, "mainapp/profile_page.html", content)


@login_required
@require_POST
def book_like(request):
    book_id = request.POST.get("id")
    action = request.POST.get("action")
    if book_id and action:
        try:
            book = get_object_or_404(Users_books, id=book_id)
            if action == "like":
                book.likes.add(request.user)
            else:
                book.likes.remove(request.user)
            return JsonResponse({"status": "ok"})
        except Users_books.DoesNotExist:
            pass
        return JsonResponse({"status": "error"})


def test(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        if name == "Alex" and password == "aiupwzqp12":
            return JsonResponse({"status": "ok", "message": "Hello Alex"})
        else:
            return JsonResponse({"status": "error"})

    return render(request, "mainapp/test.html")
