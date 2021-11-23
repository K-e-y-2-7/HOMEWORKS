from django.contrib import admin

from .models import Author, Reader, Book, Article, AuthorArticle, Like, DisLike, Comment

admin.site.register(Author)
admin.site.register(Reader)
admin.site.register(Book)

admin.site.register(Article)
admin.site.register(AuthorArticle)
admin.site.register(Like)
admin.site.register(DisLike)
admin.site.register(Comment)
