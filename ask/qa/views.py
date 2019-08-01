# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator
from qa.models import Question, Answer, QuestionManager
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.

from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def new_questions(request):
	qs = QuestionManager.new(Question.objects.all())
	try:
		limit = int(request.GET.get('limit', 10))
	except:
		limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except:
		page = 1
	paginator = Paginator(qs, limit)
	paginator.baseurl = reverse('new-questions') + '?page='
	page = paginator.page(page)
	return render(request, 'new_questions.html',
		{'title' : qs.title,
		'questions' : page.object_list,
		'paginator' : paginator,
		'page' : page,}
	)

def popular_questions(request):
	qs = Question.objects.popular(Question.objects.all())
	try:
		limit = int(request.GET.get('limit', 10))
	except:
		limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except:
		page = 1
	paginator = Paginator(qs, limit)
	paginator.baseurl = reverse('popular-questions') + '?page='
	page = paginator.page(page)
	return render(request, 'popular_questions.html',
		{'title' : qs.title,
		'questions' : page.object_list,
		'paginator' : paginator,
		'page' : page,}
	)

def question_details(request, id):
	try:
		qs = Question.objects.get(id = id)
	except Question.DoesNotExist:
		raise Http404

	return render(request, 'question_details.html',
		{'title' : qs.title,
		'text' : qs.text,
		'answers' : qs.answer_set.all()}
	)
