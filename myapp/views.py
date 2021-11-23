from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
import random
import string
from .models import Author, Reader, Book, Article, AuthorArticle, Like, DisLike, Comment


def generate_random_string(length = 10):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


users_dict = {
        'user1': 'Коля',
        'user2': 'Толя',
        'user3': 'Вася',
        'user4': 'Настя',
        'user5': 'Петя',       
        'user6': 'Славик',
        'user7': 'Наташа',
        'user8': 'Олег',
        'user9': 'Вика',
        'user10': 'Влад',
        'user11': 'Кирилл',
    } 

def home(request):
    list_for_random = range(100)
    rand_str = generate_random_string()
    return render(request, 'home.html',{
        'list_for_random': list_for_random,
        'rand_str': rand_str,
    })
    

def users(request):
    return render (request, 'users.html', {
        'my_dict' : users_dict
    })


def user(request, user_number):
    if user_number <= 11:
        key = 'user' + str(user_number)
        value = users_dict[key]
    else:
        value = 'Нет юзера с таким номером'

    return render (request, 'user.html', {
        'my_value' : value
    })


def book_library(request):
    books = Book.objects.order_by('title')
    authors = Author.objects.all()
    readers= Reader.objects.all()
    return render (request, 'BookLibrary.html',{
       'books' : books,
       'authors' : authors,
       'readers' : readers
    })

def articles(request):
    article = Article.objects.all()
    authors = AuthorArticle.objects.all()
    comment= Comment.objects.all()
    like = Like.objects.all()
    dislike= DisLike.objects.all()

    return render (request, 'articles.html',{
        'article': article,
        'authors': authors,
        'comment': comment,
        'like': like,
        'dislike': dislike,
    })


def archive_article(request):
    return render (request, 'archive_articles.html')


def article_in_archive(request, article_number): 
    return HttpResponse(f'Article in archive #{article_number}')


def  article_in_list(request, article_number, slug_text=''):
    return render (request, 'article_in_list.html', {
        'my_num' : article_number,
        'my_text' : slug_text
    })


def regex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")
