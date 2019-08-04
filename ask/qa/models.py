# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.

class Question(models.Model):
	title = models.CharField(default="", max_length=1024)
	text = models.TextField(default="")
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User, related_name='likes_set')
	
	def get_url(self):
        	return "/question/{}/".format(self.id)
	
	def __unicode__(self) :
    		return self.title

class Answer(models.Model):
	text = models.TextField(default="")
	added_at = models.DateField(auto_now_add=True)
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	
	def __unicode__(self) :
		return 'Answer by {}'.format(self.author)

