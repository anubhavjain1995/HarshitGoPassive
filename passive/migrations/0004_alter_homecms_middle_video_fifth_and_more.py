# Generated by Django 4.0.4 on 2022-06-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passive', '0003_alter_homecms_video_top'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecms',
            name='middle_video_fifth',
            field=models.ImageField(blank=True, upload_to='home_cms'),
        ),
        migrations.AlterField(
            model_name='homecms',
            name='middle_video_first',
            field=models.ImageField(blank=True, upload_to='home_cms'),
        ),
        migrations.AlterField(
            model_name='homecms',
            name='middle_video_fourth',
            field=models.ImageField(blank=True, upload_to='home_cms'),
        ),
        migrations.AlterField(
            model_name='homecms',
            name='middle_video_second',
            field=models.ImageField(blank=True, upload_to='home_cms'),
        ),
        migrations.AlterField(
            model_name='homecms',
            name='middle_video_third',
            field=models.ImageField(blank=True, upload_to='home_cms'),
        ),
        migrations.AlterField(
            model_name='homecms',
            name='slide_first_video',
            field=models.ImageField(blank=True, upload_to='home_cms'),
        ),
        migrations.AlterField(
            model_name='homecms',
            name='slide_second_video',
            field=models.ImageField(blank=True, upload_to='home_cms'),
        ),
        migrations.AlterField(
            model_name='homecms',
            name='slide_third_video',
            field=models.ImageField(blank=True, upload_to='home_cms'),
        ),
        migrations.AlterField(
            model_name='homecms',
            name='video_top',
            field=models.ImageField(blank=True, upload_to='home_cms'),
        ),
        migrations.AlterField(
            model_name='homecmsclientsslider',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_pictures'),
        ),
    ]
