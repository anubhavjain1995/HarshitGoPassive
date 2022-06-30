from django.urls import path
from .views import *
from .CmsViews import CmsViews
from .AdminViews import AdminViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , home , name='home'),
    path('home-cms/',CmsViews.as_view()),
    path('admin/',AdminViews.as_view()),
    #path('adminLogin/',AdminViews.as_view()),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
