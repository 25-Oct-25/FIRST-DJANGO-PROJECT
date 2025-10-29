from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def home_view(request: HttpRequest):
    return HttpResponse("Hello, welcome to the First Django Project!")

def about_view(request: HttpRequest):
    content = request.get_full_path()
    return HttpResponse(f"This is the about page of the First Django Project. You are at: {content}")