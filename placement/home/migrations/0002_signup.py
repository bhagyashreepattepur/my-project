# Generated by Django 4.1 on 2022-10-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=90)),
                ('password', models.CharField(max_length=90)),
                ('DOB', models.DateField(max_length=8)),
                ('gender', models.CharField(max_length=90)),
                ('phone', models.IntegerField(max_length=90)),
                ('place', models.CharField(max_length=90)),
            ],
        ),
    ]
