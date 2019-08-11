from django import forms
from .models import Question, Answer

class AskForm(forms.Form):
  title = forms.CharField(max_length=120)
  text = forms.CharField(widget=forms.Textarea)
  
  def save(self):
    question = Question.objects.create(**self.cleaned_data)
    return question

AnswerForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea)
  question = forms.IntegerField(widget=forms.HiddenInput)
  
  def save(self):
    answer = Answer.objects.create(**self.cleaned_data)
    return answer
