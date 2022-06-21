from django.urls import path
from .views import *
from .CmsViews import CmsViews

urlpatterns = [
    path('' , home , name='home'),
    path('home-cms/',CmsViews.as_view()),
]
