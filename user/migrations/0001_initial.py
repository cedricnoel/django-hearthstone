# Generated by Django 2.2.dev20181026085935 on 2018-10-26 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0004_auto_20181005_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cards', models.ManyToManyField(to='cards.Card')),
            ],
        ),
    ]