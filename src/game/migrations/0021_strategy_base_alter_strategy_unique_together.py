# Generated by Django 4.1.3 on 2023-03-07 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0020_basestrategy_alter_strategy_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='base',
            field=models.ForeignKey(default='leadership', on_delete=django.db.models.deletion.CASCADE, to='game.basestrategy'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='strategy',
            unique_together={('game', 'base')},
        ),
    ]
