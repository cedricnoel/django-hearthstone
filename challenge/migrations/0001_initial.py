# Generated by Django 2.2.dev20190116205049 on 2019-01-16 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decks', '0007_auto_20190116_2054'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=200)),
                ('deck1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='challenger_deck', to='decks.Deck')),
                ('deck2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='challenged_deck', to='decks.Deck')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenger', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenged', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='wins', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]