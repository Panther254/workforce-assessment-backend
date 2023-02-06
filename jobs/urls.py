from django.urls import path
from .views import JobListCreateView, JobApplicationListCreateView


urlpatterns = [
	path('available-jobs', JobListCreateView.as_view()),
	path('post-job', JobListCreateView.as_view()),
	path('apply-job', JobApplicationListCreateView.as_view()),
	path('list-applied-jobs', JobApplicationListCreateView.as_view()),
]


