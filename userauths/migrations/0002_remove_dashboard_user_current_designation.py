# Generated by Django 5.0 on 2024-02-05 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard_user',
            name='current_designation',
        ),
    ]
