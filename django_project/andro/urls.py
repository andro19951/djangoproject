from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="main_view"),
    url(r'^blog/', views.blog, name="blog"),
    url(r'^survey/', views.survey, name="survey"),
    url(r'^task/(?P<task_id>[0-9]+)$', views.task, name="task"),
    url(r'^task/test/(?P<test_id>[0-9]+)$', views.test, name="test_view"),
    url(r'^register/', views.register, name="register"),
    url(r'^login/$', views.logine, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^about/$', views.about, name='about'),
    url(r'^cv/$', views.cv, name='cv'),
    url(r'^why/$', views.why, name='whydo'),
    url(r'^quiz/(?P<quiz_id>[0-9]+)$', views.quiz, name="quiz_ide"),
    url(r'^quiz/', views.allquiz, name="all_quizez"),
    url(r'^generate/', views.generator, name="ylenerator"),
    url(r'^generated/', views.showall, name="yleobagenerated"),
    url(r'^generatedtext/(?P<task_id>[0-9]+)$', views.showspecific, name="yleobageneratedtext"),
    url(r'^bina/', views.bina, name="bina")

]
