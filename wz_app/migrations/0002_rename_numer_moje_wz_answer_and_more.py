# Generated by Django 5.0.1 on 2024-03-07 19:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wz_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moje_wz',
            old_name='numer',
            new_name='answer',
        ),
        migrations.RemoveField(
            model_name='moje_wz',
            name='moja_lista',
        ),
        migrations.AddField(
            model_name='moje_wz',
            name='question',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]