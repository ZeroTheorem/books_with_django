from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, 'mainapp/compleated_page.html')


def page_in_process(request):
    return render(request, 'mainapp/process_page.html')
