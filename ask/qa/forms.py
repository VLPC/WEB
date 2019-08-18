from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class AskForm(forms.Form):
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea)
	
	def clean_title(self):
		title = self.cleaned_data['title']
		if title.strip() == '':
			raise forms.ValidationError('Title is empty', code='validation_error')
		return title
	
	def clean_text(self):
		text = self.cleaned_data['text']
		if text.strip() == '':
			raise forms.ValidationError('Text is empty', code='validation_error')
		return text
	
	def save(self):
		if self._user.is_anonymous():
			self.cleaned_data['author_id'] = 1
		else:
			self.cleaned_data['author'] = self._user
		question = Question(**self.cleaned_data)
		question.save()
		return question


class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput)
	
	def clean_text(self):
		text = self.cleaned_data['text']
		if text.strip() == '':
			raise forms.ValidationError('Text is empty', code='validation_error')
		return text
	
	def clean_question(self):
		try:
			question = int(self.cleaned_data['question'])
		except ValueError:
			raise forms.ValidationError('Invalid data', code='validation_error')
		return question
	
	def save(self):
		if self._user.is_anonymous():
			self.cleaned_data['author_id'] = 1
		else:
			self.cleaned_data['author'] = self._user
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer
	
class SignupForm(forms.Form):
	username = forms.CharField(max_length=255, required=False)
	email = forms.EmailField(required=False)
	password = forms.CharField(widget=forms.PasswordInput, required=False)
	
	def clean_username(self):
		username = self.cleaned_data['username']
		if username.strip() == '':
			raise forms.ValidationError('Username is empty', code='validation_error')
		return username
	
	def clean_email(self):
		email = self.cleaned_data['email']
		if email.strip() == '':
			raise forms.ValidationError('Email is empty', code='validation_error')
		return email
	
	def clean_password(self):
		password = self.cleaned_data['password']
		if password.strip() == '':
			raise forms.ValidationError('Password is empty', code='validation_error')
		return password
	
	def save(self):
		user = User(**self.cleaned_data)
		user.save()
		return user
	
class LoginForm(forms.Form):
	username = forms.CharField(max_length=255, required=False)
	password = forms.CharField(widget=forms.PasswordInput, required=False)
	
	def clean_username(self):
		username = self.cleaned_data['username']
		if username.strip() == '':
			raise forms.ValidationError('Username is empty', code='validation_error')
		return username
	
	def clean_password(self):
		password = self.cleaned_data['password']
		if password.strip() == '':
			raise forms.ValidationError('Password is empty', code='validation_error')
		return password
