# Generated by Django 4.2.7 on 2023-11-10 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
