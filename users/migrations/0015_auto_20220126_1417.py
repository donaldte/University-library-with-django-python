# Generated by Django 3.2.9 on 2022-01-26 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_sendfeedback'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ebooks',
            options={'ordering': ['-date_added'], 'verbose_name': 'Ebook', 'verbose_name_plural': 'Ebooks'},
        ),
        migrations.CreateModel(
            name='CommandBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comand_date', models.DateTimeField(auto_now=True)),
                ('confirm', models.BooleanField(default=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.books')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
