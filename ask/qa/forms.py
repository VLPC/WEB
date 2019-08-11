from django import forms
from .models import Question, Answer

class AskForm(forms.Form):
  title = forms.CharField(max_length=120)
  text = forms.CharField(widget=forms.Textarea)
  
  def save(self):
    question = Question(**self.cleaned_data)
    return question
  
  def clean(self): pass

AnswerForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea)
  question = forms.IntegerField(widget=forms.HiddenInput)
  
  def save(self):
    answer = Answer(**self.cleaned_data)
    return answer
  
  def clean(self): pass
