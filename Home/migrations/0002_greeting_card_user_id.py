# Generated by Django 3.2.9 on 2021-12-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='greeting_card',
            name='user_id',
            field=models.TextField(default=0),
        ),
    ]