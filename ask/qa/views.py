# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.

from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def new_questions(request):
	qs = Question.objects.all().order_by('-added_at')
	
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10
	
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	
	paginator = Paginator(qs, limit)
	
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)

	return render(request, 'new.html', {'page': page})

def popular_questions(request):
	qs = Question.objects.all().order_by('-rating')
	
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10
	
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	
	paginator = Paginator(qs, limit)
	
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	
	return render(request, 'popular.html',{'page': page})

def question_details(request, pk):		
	try:
		qs = Question.objects.get(id = pk)
	except Question.DoesNotExist:
		raise Http404
	
	answers = qs.answer_set.all()
	
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid():
			form._user = request.user
			answer = form.save()
			url = answer.get_url()
			return HttpResponseRedirect(url)
			
	else: 
		form = AnswerForm(initial = {'question': qs.id})
	
	return render(request, 'details.html',
		      {'questions' : qs,
		       'answers' : answers,
		       'form' : form})

def ask(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		if form.is_valid():
			form._user = request.user
			question = form.save()
			url = question.get_url()
			return HttpResponseRedirect(url)
			
	else:
		form = AskForm()
	
	return render(request, 'question_add.html', {'form' : form})
