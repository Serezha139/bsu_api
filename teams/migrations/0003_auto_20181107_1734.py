# Generated by Django 2.1.3 on 2018-11-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(null=True, to='teams.Player'),
        ),
    ]
