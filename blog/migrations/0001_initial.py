# Generated by Django 3.1.14 on 2023-11-28 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=200)),
                ('Lastname', models.CharField(max_length=200)),
                ('Middlename', models.CharField(max_length=200)),
                ('Username', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
    ]
