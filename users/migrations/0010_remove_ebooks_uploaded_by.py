# Generated by Django 3.2.9 on 2022-01-08 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20220102_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebooks',
            name='uploaded_by',
        ),
    ]