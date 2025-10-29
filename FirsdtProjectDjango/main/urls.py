from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path("path/to/view/", views.page_view, name="page_view"),
]