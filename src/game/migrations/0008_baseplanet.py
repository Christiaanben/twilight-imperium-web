# Generated by Django 4.1.3 on 2022-12-12 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_basetile_faction'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePlanet',
            fields=[
                ('id', models.SlugField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('resource', models.PositiveSmallIntegerField()),
                ('influence', models.PositiveSmallIntegerField()),
                ('trait', models.CharField(choices=[('cultural', 'Cultural'), ('hazardous', 'Hazardous'), ('industrial', 'Industrial')], default=None, max_length=10, null=True)),
                ('technology', models.CharField(choices=[('biotic', 'Biotic'), ('warfare', 'Warfare'), ('propulsion', 'Propulsion'), ('cybernetic', 'Cybernetic')], default=None, max_length=10, null=True)),
                ('base_tile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.basetile')),
            ],
            options={
                'verbose_name': 'BasePlanet',
                'verbose_name_plural': 'BasePlanets',
                'default_related_name': 'base_planets',
            },
        ),
    ]
