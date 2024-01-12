# Generated by Django 3.1.14 on 2024-01-12 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20240112_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='prev_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemon_entities.pokemon', verbose_name='Из кого эволюционировал'),
        ),
    ]
