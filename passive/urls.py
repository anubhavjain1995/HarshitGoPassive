from django.template.defaulttags import url
from django.urls import path
from .views import *
from .CmsViews import CmsViews
from .AdminViews import AdminViews
from django.conf import settings
from .TestimonialViews import TestimonailViews
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'testimonial',TestimonailViews,basename='testimonial')

urlpatterns = [
    path('' , home , name='home'),
    path('registration' , registration , name='registration'),
    path('admin-login' , adminLogin , name='adminLogin'),
    path('admin-change-password' , admin_change_password , name='admin_change_password'),
    path('admin_profile' , admin_profile , name='admin_profile'),
    path('delete_user' , delete_user , name='delete_user'),
    path('user_change_password' , user_change_password , name='user_change_password'),
    path('user_login' , userLogin , name='userLogin'),
    path('user_registration' , user_registration , name='user_registration'),

    path('home-cms/',CmsViews.as_view()),
    path('admin/',AdminViews.as_view()),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+= router.urls