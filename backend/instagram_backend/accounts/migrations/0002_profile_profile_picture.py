# Generated by Django 3.1.7 on 2021-04-06 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profile_pictures/'),
        ),
    ]
