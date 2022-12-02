# Generated by Django 4.1.3 on 2022-11-22 18:23

import django.core.validators
from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_lobby_id_alter_lobby_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lobby',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet=None, length=8, max_length=8, prefix='', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lobby',
            name='name',
            field=models.CharField(default='', max_length=30, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]