from django.contrib import admin

# Register your models here.
from andro.models import Blog, Questions,Answers,Texts,Task,QuestionType,User, Quiz

admin.site.register(Blog)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Texts)
admin.site.register(Task)
admin.site.register(QuestionType)
admin.site.register(User)
admin.site.register(Quiz)
