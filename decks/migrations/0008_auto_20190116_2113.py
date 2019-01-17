# Generated by Django 2.2.dev20190116205855 on 2019-01-16 21:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0010_auto_20190116_2054'),
        ('decks', '0007_auto_20190116_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='items',
        ),
        migrations.AlterField(
            model_name='deck',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 16, 21, 13, 55, 704831)),
        ),
        migrations.CreateModel(
            name='Deck_cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Card')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decks.Deck')),
            ],
        ),
    ]