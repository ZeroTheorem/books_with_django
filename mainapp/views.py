import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from mainapp.models import Users_books
from django.http import HttpResponse
from my_authapp.models import UserProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


@login_required
def get_all_book(request):
    result = Users_books.objects.filter(owner=request.user)
    books = len(result)
    pages = sum((x.total_page for x in result))
    paginator = Paginator(result, 10)
    page_number = request.GET.get("page", 1)
    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
        return HttpResponse("")
    except PageNotAnInteger:
        page = paginator.page(1)
    if int(page_number) > 1:
        return render(
            request,
            "mainapp/books_list.html",
            {"page": page},
        )

    return render(
        request,
        "mainapp/compleated_page.html",
        {"page": page, "books": books, "pages": pages},
    )


@login_required
@require_POST
def create_or_delete_book(request):
    if request.POST.get("book_id"):
        Users_books.objects.filter(pk=request.POST["book_id"]).delete()
        os.remove(os.path.join(settings.MEDIA_ROOT, request.POST["delete_book_image"]))
        return redirect("mainapp:copleated_book")
    else:
        book = Users_books(
            owner=request.user,
            book_name=request.POST["book_name"],
            author_name=request.POST["author_name"],
            year_of_writing=request.POST["year_of_writing"],
            total_page=request.POST["total_page"],
            description=request.POST["description"],
            book_image=request.FILES["book_image"],
        )
        book.save()
        return redirect("mainapp:copleated_book")


def profile_page(request):
    result = Users_books.objects.filter(owner=request.user)
    pages = sum((x.total_page for x in result))
    content = {"books": len(result), "pages": pages}
    return render(request, "mainapp/profile_page.html", content)


def users_list(request):
    profiles = UserProfile.objects.exclude(user_id=request.user.id)
    return render(request, "mainapp/users_list.html", {"profiles": profiles})
