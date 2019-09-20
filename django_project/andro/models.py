from django.db import models


# Create your models here.
class Blog(models.Model):
    def default_lol(self):
        return self.blog_title

    blog_title = models.CharField(max_length=250)
    blog_logo = models.ImageField(upload_to='static/assets/css/images')
    blog_description = models.TextField(max_length=100000)
    blog_text = models.TextField(max_length=100000)


class Questions(models.Model):
    def default(self):
        return self.Question

    Question = models.CharField(max_length=2500)
    answer = models.CharField(max_length=2500)


class Answers(models.Model):
    def default(self):
        return self.answer

    question = models.CharField(max_length=2500)
    answer = models.CharField(max_length=2500)
    user_id = models.CharField(max_length=2500)


class Task(models.Model):
    def default(self):
        return 'task is equal to:'+self.name

    name = models.CharField(max_length=250)
    description = models.CharField(max_length=2500)
    url = models.CharField(max_length=2500)


class QuestionType(models.Model):
    def default(self):
        return "NONE"

    task_id = models.ForeignKey("Texts", on_delete=models.CASCADE)
    Questions = models.CharField(max_length=2500)
    Answer1 = models.CharField(max_length=2500)
    Answer2 = models.CharField(max_length=2500)
    Answer3 = models.CharField(max_length=2500)
    Answer4 = models.CharField(max_length=2500)
    rightone = models.CharField(max_length=5)
    Answers = models.CharField(max_length=2500)
    imaged = models.CharField(max_length=2500)


class Texts(models.Model):
    def default(self):
        return "None"

    text_id = models.ForeignKey("Task", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/assets/css/textimages')
    text = models.TextField(max_length=3500)


class User(models.Model):
    def default(self):
        return "None"
    score = models.IntegerField(default=0, blank=True, null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    progress = models.IntegerField()
class Quiz(models.Model):
    def default(self):
        return "None"
    quiz_id=models.IntegerField(default=0, blank=True, null=True)
    img=models.CharField(max_length=250)
    catchphrase=models.CharField(max_length=250)