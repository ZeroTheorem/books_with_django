from django.shortcuts import render
from mainapp.models import Users_books
from authnapp.models import my_User
# Create your views here.


def main_page(request):
    if request.method == "POST":
        book = Users_books(owner=request.user,
                    book_name=request.POST["book_name"],
                    author_name=request.POST["author_name"],
                    year_of_writing=request.POST["year_of_writing"],
                    total_page=request.POST["total_page"],
                    current_page=request.POST["current_page"],
                    description=request.POST["description"],)
        book.save()
        return render(request, 'mainapp/compleated_page.html')

    else:
        if request.user.is_authenticated:
            result = Users_books.objects.filter(owner=request.user)
            content = {"result": result}
            return render(request, 'mainapp/compleated_page.html', content)
        return render(request, 'mainapp/compleated_page.html')


def page_in_process(request):
    return render(request, 'mainapp/process_page.html')
