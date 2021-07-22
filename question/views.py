from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.contrib.auth.decorators import login_required

# Create your views here.

def question_list(request):
    all_questions = Question.objects.all()
    print(all_questions)
    return render(request,'question_list.html',{'questions':all_questions})

@login_required(login_url='authentication:login')
def question_detail(request,question_slug = None):
    print(request.user.user_profile)
    if request.user.user_profile.is_subscribed:
        question = Question.objects.get(slug = question_slug)
        file_path = question.question_file
        f = open("static/media/"+str(file_path), 'r')
        file_content = f.read()
        f.close()
        print(file_content)
        return render(request,'question_detail.html',{'question':question,'question_description':file_content})
    

def read_file(request):
    question = Question.objects.get(id=2)
    print("question is ",question)
    file_path = question.question_file
    f = open("static/media/"+str(file_path), 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")