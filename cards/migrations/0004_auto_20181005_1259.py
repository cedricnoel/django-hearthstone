# Generated by Django 2.2.dev20181005102959 on 2018-10-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_card_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(default='cards/static/img/no-img.jpg', upload_to='cards/static/img/'),
        ),
    ]