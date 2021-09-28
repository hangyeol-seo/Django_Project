from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import compare.views
from .models import Question


def index(request,username):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list,'username':username}
    return render(request, 'polls/index.html',context)

def question_detail(request, question_id, username):
    count=0
    question=get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/question_detail.html',
    {'question':question,'count':count,'username':username})

def vote(request, question_id,username):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/question_detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",'username':username
        })
    selected_choice.votes+=1
    selected_choice.save()

    if question_id==5:
        count=1
        return render(request, 'polls/question_detail.html',{'question':question,'username':username,
        'count':count})

    else:
        count=0
        question_id+=1
        question=get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/question_detail.html',{'question':question,'username':username,
        'count':count})
    


