from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('',views.question_list,name='question_list'),
    path('<slug:question_slug>',views.question_detail,name='question_detail'),
    path('read_file/txt',views.read_file,name='read_file'),


]