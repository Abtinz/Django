# Generated by Django 4.0.2 on 2022-03-21 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_information',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
