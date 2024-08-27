from django.urls import path
from .views import BookListView, home, BookDetailView

app_name = "books"

urlpatterns = [
    path("", home, name="home"),
    path("list/", BookListView.as_view(), name="list"),
    path("list/<pk>", BookDetailView.as_view(), name="detail"),
]
