# Generated by Django 4.2.16 on 2024-11-10 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('excerpt', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('author', models.ForeignKey(default='deleted user', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]