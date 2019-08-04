# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator
from qa.models import Question, Answer
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect

# Create your views here.

from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs):
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
    return page, paginator


def new_questions(request):
    qs = Question.objects.all().order_by('-id')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('new-questions') + '?page='

    return render(request, 'new_questions.html', {
	'title' : 'New',
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

def popular_questions(request):
	qs = Question.objects.all().order_by('-rating')
	page, paginator = paginate(request, qs)
	paginator.baseurl = reverse('popular-questions') + '?page='
	
	return render(request, 'popular_questions.html',
		{'title' : 'Popular',
		'questions' : page.object_list,
		'paginator' : paginator,
		'page' : page,}
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
