import uuid as uuid
from django.db import models


# Create your models here.

class WebBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class HomeCms(WebBaseModel):
    id = models.AutoField(primary_key=True)
    video_top = models.FileField(upload_to="home_cms", blank=True, default='')
    text_top = models.TextField()

    slide_first_video = models.FileField(upload_to="home_cms", blank=True, default='')
    slide_first_header = models.TextField()
    slide_first_text = models.TextField()

    slide_second_video = models.FileField(upload_to="home_cms", blank=True, default='')
    slide_second_header = models.TextField()
    slide_second_text = models.TextField()

    slide_third_video = models.FileField(upload_to="home_cms", blank=True, default='')
    slide_third_header = models.TextField()
    slide_third_text = models.TextField()

    middle_header_first = models.CharField(max_length=100)
    middle_text_first = models.TextField()
    middle_video_first = models.FileField(upload_to="home_cms", blank=True, default='')

    middle_header_second = models.CharField(max_length=100)
    middle_text_second = models.TextField()
    middle_video_second = models.FileField(upload_to="home_cms", blank=True, default='')

    middle_header_third = models.CharField(max_length=100)
    middle_text_third = models.TextField()
    middle_video_third = models.FileField(upload_to="home_cms", blank=True, default='')

    middle_header_fourth = models.CharField(max_length=100)
    middle_text_fourth = models.TextField()
    middle_video_fourth = models.FileField(upload_to="home_cms", blank=True, default='')

    middle_header_fifth = models.CharField(max_length=100)
    middle_text_fifth = models.TextField()
    middle_video_fifth = models.FileField(upload_to="home_cms", blank=True, default='')

    bottom_header = models.CharField(max_length=100)
    bottom_text = models.TextField()


# change table name as testimonial
class HomeCmsClientsSlider(WebBaseModel):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    profile_image = models.ImageField(upload_to="profile_pictures",blank=True)
    text = models.TextField()
    username = models.CharField(max_length=100)


class AdminDataTable(WebBaseModel):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    admin_type = models.IntegerField(default=1)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to="profile_pictures",blank=True)
    token = models.CharField(max_length=255,default='')


class UserTable(WebBaseModel):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    user_type = models.IntegerField(default=0)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to="profile_pictures",blank=True)
    token = models.CharField(max_length=255,default='')
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=13)
    status = models.BooleanField(default=True)
    agent_code = models.CharField(max_length=15, default='')
    referred_agent_id = models.CharField(max_length=50, default='')


class UserLeadsTable(WebBaseModel):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=13)
    message = models.CharField(max_length=100)


class ChangesRequestTable(WebBaseModel):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField()
    message = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
