# Generated by Django 3.2.9 on 2021-11-23 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20211121_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='reader',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='dislike',
            name='article',
        ),
        migrations.RemoveField(
            model_name='dislike',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='dislike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='like',
            name='article',
        ),
        migrations.RemoveField(
            model_name='like',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='AuthorArticle',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='DisLike',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Reader',
        ),
    ]
