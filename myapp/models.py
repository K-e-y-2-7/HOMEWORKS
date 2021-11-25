import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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
   author = models.ManyToManyField(Author)
   are_available = models.BooleanField(default=True)
   title = models.CharField(max_length=100)
   reader = models.ManyToManyField(Reader)
   year_of_public = models.DateField()

   class Meta:
        ordering = ['title']
        
   def __str__(self):
        return self.title


class AuthorArticle(models.Model):
   name = models.CharField(max_length=120)
   pseudonym = models.CharField(max_length=120, blank=True, null=True)

   def __str__(self):
      return self.name


class Article(models.Model):
   author = models.ForeignKey(AuthorArticle, on_delete=models.CASCADE, null=True,
                              related_name='articles')
   created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
   genre = models.CharField(max_length=100, default='')
   headline = models.CharField(max_length=100)
   text = models.TextField(max_length=10000, null=True)
   updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

   class Meta:
      ordering = ['headline']

   def __str__(self):
      return f"Headline - {self.headline}, Author - {self.author.name}, genre - {self.genre}, id - {self.id}"


class Comment(models.Model):
   article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.DO_NOTHING)
   comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING,
                              related_name='comments')
   created_at = models.DateField(null=True, blank=True,)
   text = models.CharField(max_length=2000, null=True, blank=True)
   user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.DO_NOTHING)

   def __str__(self):
      return f'{self.text} by {self.user} id {self.id}  created at { self.created_at} '
      
   def save(self, **kwargs):
        if not self.id:
            self.created_at = timezone.now() - datetime.timedelta(weeks=52, days=1)
        super().save(**kwargs)


class Like(models.Model):
   article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.DO_NOTHING)
   comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.DO_NOTHING)
   user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
       
   def __str__(self):
        return f"By user {self.user.username}"
    

class DisLike(models.Model):
   article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.DO_NOTHING)
   comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.DO_NOTHING)
   user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)

   def __str__(self):
        return f"By user {self.user.username}"
