# Generated by Django 2.2.dev20190117195639 on 2019-01-17 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='social',
            old_name='owner',
            new_name='user',
        ),
    ]
