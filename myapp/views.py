import random
import string
from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

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
    return render (request, 'book_library.html',{
       'books' : books,
       'authors' : authors,
       'readers' : readers
    })


def articles(request):
    article = Article.objects.all()
    authors = AuthorArticle.objects.all()
    comment= Comment.objects.filter(comment__range = (-5, -1))
    like = Like.objects.all()
    dislike= DisLike.objects.all()

    return render (request, 'articles.html',{
        'article': article,
        'authors': authors,
        'comment': comment,
        'like': like,
        'dislike': dislike,
    })


def last_five_сomments(request):
    comment= Comment.objects.order_by('-id')[:5]

    return render (request, 'last_five_сomments.html',{        
        'comment': comment,
    })


def five_comments (request):
    default_user = User.objects.get(id=1)
    comment1 = Comment.objects.create( text='Start of this comment. Some text...', user = default_user )
    comment2 = Comment.objects.create( text='A large comment ... ', user = default_user)
    comment3 = Comment.objects.create( text='Some text .. here is Middle of this comment. Some random text ...', user = default_user)
    comment4 = Comment.objects.create( text='Some random text...', user = default_user)
    comment5 = Comment.objects.create( text='Some text... Here the comment Finish.', user = default_user)

    #Comment.objects.filter(text__istartswith = 'Start').update(text = 'bla-bla')
    #Comment.objects.filter(text__iendswith = 'Finish.').update(text = 'ta-ta-ta') 
    #Comment.objects.filter(text__icontains='k').exclude(text__icontains='c').delete()

    #Comment.objects.filter(сomment__user__id ='1').exclude(text__icontains='some').filter(created_at__gte__=datetime.today)
    return render (request, 'five_comments.html',{        
        'comment1': comment1,
        'comment2': comment2,
        'comment3': comment3,
        'comment4': comment4,
        'comment5': comment5,
    })

def сomment_one_year_ago(request):
    comment= Comment.objects.order_by('-id')[:5]

    return render (request, 'сomment_one_year_ago.html',{        
        'comment': comment,
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


def two_сomments_of_article(request):
    author_art = AuthorArticle.objects.order_by('-pseudonym')[:1]
    for elem in author_art:
        author_art = elem.name
    
    article = article = Article.objects.filter(author__pseudonym__icontains = author_art)

    comment= Comment.objects.filter(article__author__pseudonym__icontains=author_art).order_by('created_at')[:2]
    return render (request, 'two_сomments_of_article.html',{        
        'author_art': author_art,
        'comment': comment,
        'article' : article
    })



