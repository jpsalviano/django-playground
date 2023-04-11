from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>", views.ReadArticleView.as_view(), name="read_article"),
    path("create_article", views.CreateArticleView.as_view(), name="create_article"),
]
