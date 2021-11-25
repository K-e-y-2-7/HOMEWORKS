"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib import admin

from myapp.views import users, user, regex, home, book_library, five_comments, last_five_сomments, сomment_one_year_ago, two_сomments_of_article

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('book_library/', book_library, name='book_library'),
    path('users/', users, name='users'),
    path('users/<int:user_number>', user, name='user'),   
    path('article/', include('myapp.urls')),
    path('last_five_сomments', last_five_сomments, name='last_five_сomments' ),
    path('сomment_one_year_ago', сomment_one_year_ago, name='сomment_one_year_ago' ),
    path('two_сomments_of_article', two_сomments_of_article, name='two_сomments_of_article' ),
    path('five_comments', five_comments, name='five_comments' ),
    re_path(r'^(?P<text>[\dabc+def]{4}-[\dabc+def]{6}$)', regex, name='regex'), #иероглефы ^ - start of string $- end of string

]

