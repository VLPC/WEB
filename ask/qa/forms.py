from django import forms

class AskForm(forms.Form):
  title = forms.CharField(max_length = 120)
  text = forms.CharField(widget = forms.Textarea)
  
  def clean(self):
    pass
  
  def save(self):
    question = Question(**self.cleaned_data)
    question.save()
    return question

AnswerForm
  text = forms.CharField(widget = forms.Textarea)
  question = forms.IntegerField(widget=forms.HiddenInput)
  
  def clean(self):
    pass
  
  def save(self):
    answer = Answer(**self.cleaned_data)
    answer.save()
    return answer
