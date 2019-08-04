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
	page = request.GET.get('page')
	paginator = Paginator(qs, 10)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
    
	paginator.baseurl = reverse('new-questions') + '?page='

	return render(request, 'new_questions.html', {
	'title' : 'New',
        'questions': page.object_list,
    })

def popular_questions(request):
	qs = Question.objects.all().order_by('-rating')
	page = request.GET.get('page')
	paginator = Paginator(qs, 10)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	paginator.baseurl = reverse('popular-questions') + '?page='
	
	return render(request, 'popular_questions.html',
		      {'title' : 'Popular',
		       'questions' : page.object_list,}
	)

def question_details(request, num):
	try:
		qs = Question.objects.get(id = num)
	except Question.DoesNotExist:
		raise Http404

	return render(request, 'question_details.html',
		{'title' : 'Details',
		'text' : qs,
		'answers' : qs.answer_set.all()}
	)
