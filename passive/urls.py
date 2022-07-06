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
    path('registration' , registration , name='registration'),#post
    path('admin-login' , adminLogin , name='adminLogin'),#post
    path('admin-change-password' , admin_change_password , name='admin_change_password'),#post
    path('admin_profile/<str:pk>/' , admin_profile , name='admin_profile'),#get
    path('delete_user/<str:pk>/' , delete_user , name='delete_user'),#delete
    path('user_change_password' , user_change_password , name='user_change_password'),#post
    path('user_login' , userLogin , name='userLogin'),#post
    path('user_registration' , user_registration , name='user_registration'),#post
    path('user_profile/<str:pk>/' , user_profile , name='user_profile'),#get

    path('home-cms/',CmsViews.as_view()),#post,get
    path('admin/',AdminViews.as_view()),#post,get


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+= router.urls