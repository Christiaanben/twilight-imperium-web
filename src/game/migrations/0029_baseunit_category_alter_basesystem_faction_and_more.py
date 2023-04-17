# Generated by Django 4.1.3 on 2023-04-17 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0028_system_activated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseunit',
            name='category',
            field=models.SlugField(choices=[('ground_force', 'Ground Force'), ('ship', 'Ship'), ('structure', 'Structure')], default='ship', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basesystem',
            name='faction',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.faction'),
        ),
        migrations.AlterField(
            model_name='baseunit',
            name='faction',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.faction'),
        ),
    ]
