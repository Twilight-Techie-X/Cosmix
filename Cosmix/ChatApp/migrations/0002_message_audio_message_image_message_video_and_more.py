# Generated by Django 5.1 on 2024-08-18 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audios/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg'])]),
        ),
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
        migrations.AddField(
            model_name='message',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi', 'mkv'])]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picure',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
