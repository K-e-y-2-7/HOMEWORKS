from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Reader(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    reader = models.ManyToManyField(Reader)
    are_available = models.BooleanField(default=True)
    year_of_public = models.DateField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class AuthorArticle(models.Model):
    pseudonym = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Article(models.Model):
    headline = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorArticle, on_delete=models.CASCADE, null=True,
                               related_name='articles')
    text = models.TextField(max_length=10000, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    genre = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return f"Headline - {self.headline}, Author - {self.author.name}, genre - {self.genre}, id - {self.id}"


class Comment(models.Model):
    text = models.CharField(max_length=2000, null=True, blank=True)
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING,
                                related_name='comments')
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.text} by {self.user.username} '


class Like(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.DO_NOTHING)
       
    def __str__(self):
        return f"By user {self.user.username}"
    

class DisLike(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"By user {self.user.username}"
