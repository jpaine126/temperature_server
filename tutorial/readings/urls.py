from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("readings/", views.ReadingList.as_view()),
    path("readings/<int:pk>/", views.ReadingDetail.as_view()),
    path("api/readings", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
