from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.new_questions, name='new-questions'),
	url(r'^popular/', views.popular_questions, name='popular-questions'),
	url(r'^login/', views.test, name = 'test'),
	url(r'^signup/', views.test, name = 'test'),
	url(r'^question/(?P<pk>\d+)$', views.question_details, name = 'question-details'),
	url(r'^ask/', views.test, name = 'test'),
	url(r'^new/', views.test, name = 'test'),
]
