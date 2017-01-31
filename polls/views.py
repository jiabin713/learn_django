from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):

    return HttpResponse("polls的首页")


def detail(request, question_id):
    return HttpResponse("你正在看question {}，的详细页".format(question_id))

def results(request, question_id):
    return HttpResponse("你在看问题{}的投票结果".format(question_id))

def vote(request, question_id):
    return HttpResponse("你在给问题{}投票".format(question_id))

