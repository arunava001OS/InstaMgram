# Generated by Django 3.1.7 on 2021-03-26 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210326_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_images/'),
        ),
    ]