from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("quickstart/", views.TempReadingList.as_view()),
    path("quickstart/<int:pk>/", views.TempReadingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)