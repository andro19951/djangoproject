# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Blog, Questions, Answers, Task, Texts, QuestionType, Quiz
import uuid as ui
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    all_tasks = Task.objects.all().order_by('-id')
    context = dict(all_tasks=all_tasks)
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def cv(request):
    return render(request, 'cv.html')


def blog(request):
    all_blogs = Blog.objects.all().order_by('-id')
    context = dict(all_blogs=all_blogs)
    return render(request, 'blog.html', context)

def bina(request):
    return render(request, 'task/bina.html')


def survey(request):
    all_questions = Questions.objects.all().order_by('-id')
    all_answers = Answers.objects.all().order_by('-id')
    context = dict(all_questions=all_questions, all_answers=all_answers)
    for key in request.POST:
        question = Questions()
        question.Question_id = key
        question.answer = request.POST[key]
        answer = Answers()
        answer.user_id = ui.UUID.time
        answer.question = question.Question_id
        answer.answer = question.answer
        answer.save()
    return render(request, 'survey.html', context)


def task(request, task_id):
    try:
        all_text = Texts.objects.filter(text_id=task_id)
    except Texts.DoesNotExist:
        raise Http404("Event does not exist")
    context = dict(all_text=all_text)
    return render(request, 'tasks/' + task_id + '.html', context)

def allquiz(request):
    all_quiz_text = Quiz.objects.all().order_by('-id')
    context = dict(all_quiz_text=all_quiz_text)
    return render(request, 'quizes.html', context)

def quiz(request, quiz_id):
    try:
        quiz_text = Quiz.objects.get(quiz_id=quiz_id)
    except Texts.DoesNotExist:
        raise Http404("Event does not exist")
    context = dict(quiz_text=quiz_text)
    return render(request, 'gaige.html', context)

def register(request):
    all_users = User.objects.all().order_by('-id')
    for user in all_users:
        if (user.username == request.POST.get('usernamed')):
            message = "username is taken!!!"
            return render(request, 'register.html', dict(message=message))

        if (user.email == request.POST.get('email')):
            message = "email is already used, Are you sure you do not want to log in?"
            return render(request, 'register.html', dict(message=message))
    if (request.POST.get('usernamed') and request.POST.get('email') and request.POST.get(
            'password') and request.POST.get('password2')):
        if (request.POST['password'] != request.POST['password2']):
            message = "passwords do not match!!"
        else:
            used = User.objects.create_user(request.POST.get('usernamed'), request.POST.get('email'),
                                            request.POST.get('password'))
            message = "Succesfully registered"

    else:
        message = "empty fields detected!!"
    return render(request, 'register.html', dict(message=message))

def logine(request):
    all_users = User.objects.all()
    message = "come oooon"

    for user in all_users:
        if (user.username == request.POST.get('usernamed')):
            user = authenticate(username=request.POST.get('usernamed'), password=request.POST.get('password'))
            login(request, user)
            if (user is not None):

                message = "congrats"
                return index(request)
            else:
                message = "Password is incorrect"
                return render(request, 'login.html', dict(message=message))

    return render(request, 'login.html', dict(message=message))


def logout_view(request):
    logout(request)
    all_tasks = Task.objects.all().order_by('-id')
    context = dict(all_tasks=all_tasks)
    return render(request, 'index.html', context)


def test(request, test_id):
    the_test = get_object_or_404(QuestionType, id=test_id)
    quiz=the_test.task_id.questiontype_set.order_by('id')
    k=0
    for next_test in quiz:
        if(k==1):
            context = dict(the_test=the_test, next_test=next_test)
            return render(request, "task/test.html", context)
        if(next_test==the_test):
            k=1
    context = dict(the_test=the_test)
    return render(request, "task/test.html", context)

def generator(request):
    all_generators = Task.objects.all().order_by('-id')
    for user in all_generators:
        if (user.name == request.POST.get('title')):
            message = "ტექსტის სახელი გამოყენებულია!"
            return render(request, 'register.html', dict(message=message))
    if (request.POST.get('title') and request.POST.get('url') and request.POST.get(
            'text')):
        instance=Task()
        instance.name=request.POST.get('title')
        instance.url=request.POST.get('url')
        instance.description=request.POST.get('text')
        instance.save()
        message = "Succesfully registered"

    else:
        message = "empty fields detected!!"
    return render(request, 'yleobagenerator.html', dict(message=message))

def showall(request):
    all_tasks = Task.objects.all().order_by('-id')
    context = dict(all_tasks=all_tasks)
    return render(request, 'textgenerated.html', context)

def showspecific(request, task_id):
    the_test = get_object_or_404(Task, id=task_id)
    context = dict(the_test=the_test)
    return render(request, "bullshit.html", context)

#რატომ უნდა დავიცვათ თავი?

def why(request):
    return render(request, ' why.html')
