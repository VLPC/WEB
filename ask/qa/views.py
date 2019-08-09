# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
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
	paginator.baseurl = reverse('new-questions') + '?page='
	
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)

	return render(request, 'new.html', {
        'questions': page.object_list,
	'page': page,
	'paginator': paginator}
	)

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
	paginator.baseurl = reverse('popular-questions') + '?page='
	
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	
	return render(request, 'popular.html',
		{'questions' : page.object_list,
		'page': page,
		'paginator': paginator}
	)

def question_details(request, num):
	try:
		qs = Question.objects.get(id = num)
	except Question.DoesNotExist:
		raise Http404
	
	answers = qs.answer_set.all()
	
	return render(request, 'details.html',
		{'questions' : page.object_list,
		'answers' : answers}
	)
