# Generated by Django 5.0.1 on 2024-03-24 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wz_app', '0010_alter_moje_wz_ilosc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moje_wz',
            name='Ilosc',
            field=models.IntegerField(default=0),
        ),
    ]
