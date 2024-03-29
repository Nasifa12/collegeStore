# Generated by Django 5.0.1 on 2024-01-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('DOB', models.DateField()),
                ('Age', models.IntegerField(max_length=100)),
                ('PhoneNumber', models.IntegerField(max_length=100)),
                ('MailID', models.EmailField(max_length=250)),
                ('Address', models.TextField(max_length=250)),
                ('Department', models.TextField(max_length=250)),
                ('Courses', models.CharField(max_length=250)),
                ('Purpose', models.CharField(max_length=250)),
                ('Materials', models.CharField(max_length=250)),
            ],
        ),
    ]
