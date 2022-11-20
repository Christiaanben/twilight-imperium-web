# Generated by Django 4.1.3 on 2022-11-20 14:22

import django.core.validators
from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobby',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet=None, length=10, max_length=10, prefix='', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lobby',
            name='name',
            field=models.CharField(default='', max_length=30, validators=[django.core.validators.MinLengthValidator(3, 'game.models.lobby must contain at least 3 characters')]),
        ),
    ]
