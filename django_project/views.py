from django.shortcuts import render
from .models import Blog, Questions, Answers,Task,Texts,QuestionType
import uuid as ui
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
# Create your views here.
def index(request):
    all_tasks=Task.objects.all().order_by('-id')
    context = dict(all_tasks=all_tasks)
    return  render(request, 'index.html', context)
def about(request):
    return  render(request, 'about.html')

def cv(request):
    return render(request, 'cv.html')
def blog(request):
    all_blogs=Blog.objects.all().order_by('-id')
    context = dict(all_blogs=all_blogs)
    return  render(request, 'blog.html', context)
def survey(request):
    all_questions=Questions.objects.all().order_by('-id')
    all_answers=Answers.objects.all().order_by('-id')
    context= dict(all_questions=all_questions, all_answers=all_answers)
    for key in request.POST:
        question=Questions()
        question.Question_id=key
        question.answer = request.POST[key]
        answer=Answers()
        answer.user_id=ui.UUID.time
        answer.question=question.Question_id
        answer.answer=question.answer
        answer.save()
    return render(request, 'survey.html', context)

def task(request, task_id):
    try:
        all_text=Texts.objects.filter(text_id=task_id)
    except Texts.DoesNotExist:
        raise Http404("Event does not exist")
    context = dict(all_text=all_text)
    return render(request, 'tasks/'+task_id+'.html', context)
def register(request):
    all_users=User.objects.all().order_by('-id')
    for user in all_users:
        if(user.username==request.POST.get('usernamed')):
            message="username is taken!!!"
            return render(request, 'register.html', dict(message=message))

        if (user.email == request.POST.get('email')):
            message="email is already used, Are you sure you do not want to log in?"
            return render(request, 'register.html', dict(message=message))
    if(request.POST.get('usernamed')and request.POST.get('email') and request.POST.get('password') and request.POST.get('password2')):
        if(request.POST['password']!=request.POST['password2']):
            message="passwords do not match!!"
        else:
            used=User.objects.create_user(request.POST.get('usernamed'),request.POST.get('email'),request.POST.get('password'))
            message="Succesfully registered"

    else:
        message="empty fields detected!!"
    return render(request, 'register.html', dict(message=message))

def logine(request):
    all_users=User.objects.all()
    message = "come oooon"

    for user in all_users:
        if(user.username == request.POST.get('usernamed')):
            user = authenticate(username=request.POST.get('usernamed'), password=request.POST.get('password'))
            login(request, user, backend=None)
            if(user is not None):

                message="congrats"
                return index(request)
            else:
                message="Password is incorrect"
                return render(request, 'login.html', dict(message=message))

    return render(request, 'login.html',dict(message=message))
def logout_view(request):
    logout(request)
    all_tasks=Task.objects.all().order_by('-id')
    context = dict(all_tasks=all_tasks)
    return render(request, 'index.html',context)
def test(request):
    all_tests=QuestionType.objects.all()
    context= dict(all_tests=all_tests)
    return render(request, "task/test.html", context)