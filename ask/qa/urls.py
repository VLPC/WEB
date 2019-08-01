from django.conf.urls import url
from qa.views import test, new_questions, popular_questions, question_details

urlpatterns = [
	url(r'^$', new_questions, name='new-questions'),
	url(r'^popular/', popular_questions, name='popular-questions'),
	url(r'^login/', test, name = 'test'),
	url(r'^signup/', test, name = 'test'),
	url(r'^question/(?P<index>\d+)/', question_details, name = 'question-details'),
	url(r'^ask/', test, name = 'test'),
	url(r'^new/', test, name = 'test'),
]
