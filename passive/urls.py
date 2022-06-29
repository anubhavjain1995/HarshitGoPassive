from django.urls import path
from .views import *
from .CmsViews import CmsViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , home , name='home'),
    path('home-cms/',CmsViews.as_view()),
    path('upload/' ,uploadCms, name='uploadCms' ),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
