# Generated by Django 5.2 on 2025-05-10 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='sens.jpg', null=True, upload_to=''),
        ),
    ]
