from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Hello World! This is my first Django page.")