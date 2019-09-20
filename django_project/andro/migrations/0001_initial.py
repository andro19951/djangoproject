# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=2500)),
                ('answer', models.CharField(max_length=2500)),
                ('user_id', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog_title', models.CharField(max_length=250)),
                ('blog_logo', models.ImageField(upload_to=b'static/assets/css/images')),
                ('blog_description', models.TextField(max_length=100000)),
                ('blog_text', models.TextField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Question', models.CharField(max_length=2500)),
                ('answer', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Questions', models.CharField(max_length=2500)),
                ('Answer1', models.CharField(max_length=2500)),
                ('Answer2', models.CharField(max_length=2500)),
                ('Answer3', models.CharField(max_length=2500)),
                ('Answer4', models.CharField(max_length=2500)),
                ('rightone', models.CharField(max_length=5)),
                ('Answers', models.CharField(max_length=2500)),
                ('imaged', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/assets/css/textimages')),
                ('text', models.TextField(max_length=3500)),
                ('text_id', models.ForeignKey(to='andro.Task')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('progress', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='questiontype',
            name='task_id',
            field=models.ForeignKey(to='andro.Texts'),
        ),
    ]
