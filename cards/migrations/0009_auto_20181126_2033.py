# Generated by Django 2.2.dev20181121202047 on 2018-11-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_card_owners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='deck',
            field=models.ManyToManyField(blank=True, related_name='cards', to='decks.Deck'),
        ),
    ]
