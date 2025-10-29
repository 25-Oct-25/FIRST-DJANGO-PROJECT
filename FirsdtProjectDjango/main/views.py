from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def page_view(request : HttpRequest):
    content = "content to be sen"
    return HttpResponse(content)

