# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator
from qa.models import Question, Answer, QuestionManager

# Create your views here.

from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def new_questions(request):
	questions = Question.object.new(Question.object.all())
	try:
		limit = int(request.GET.get('limit', 10))
	except:
		limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except:
		page = 1
	paginator = Paginator(questions, limit)
	page = paginator.page(page)
	return render(request, '',
		'title' : 
		'questions' : page.object_list,
		'paginator' : paginator,
		'page' : page,
	)






