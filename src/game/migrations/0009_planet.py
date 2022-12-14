# Generated by Django 4.1.3 on 2022-12-12 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_baseplanet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_exhausted', models.BooleanField(default=True)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.baseplanet')),
                ('tile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.tile')),
            ],
            options={
                'verbose_name': 'Planet',
                'verbose_name_plural': 'Planets',
                'default_related_name': 'planets',
                'unique_together': {('tile', 'base')},
            },
        ),
    ]
