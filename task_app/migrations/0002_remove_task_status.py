# Generated by Django 4.1.2 on 2022-10-08 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
