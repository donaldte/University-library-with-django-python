# Generated by Django 3.2.9 on 2022-01-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20220108_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cover',
            field=models.ImageField(blank=True, upload_to='cover'),
        ),
    ]