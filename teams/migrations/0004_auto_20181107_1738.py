# Generated by Django 2.1.3 on 2018-11-07 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20181107_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(blank=True, to='teams.Player'),
        ),
    ]
