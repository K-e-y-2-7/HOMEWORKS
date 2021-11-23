from django.urls import path
from .views import articles, archive_article, article_in_list, article_in_archive


urlpatterns = [
    path('', articles , name='articles'),
    path('archive/', archive_article, name='archive_articles'),
    path('<int:article_number>/', article_in_list, name='article'),
    path('<int:article_number>/archive', article_in_archive, name='article_in_archive'),
    path('<int:article_number>/<slug:slug_text>', article_in_list, name='article_name'),
]
