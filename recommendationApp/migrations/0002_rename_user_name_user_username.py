# Generated by Django 3.2.4 on 2021-07-04 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendationApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='username',
        ),
    ]