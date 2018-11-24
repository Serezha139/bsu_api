# Generated by Django 2.1.3 on 2018-11-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20181124_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='ongoing',
        ),
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('FEST', 'Фестиваль'), ('CUP', 'Кубок'), ('8', 'Одна Восьмая'), ('4', 'Одна Четвертая'), ('2', 'Полуфинал'), ('1', 'Финал')], default='UPCOMING', max_length=40),
        ),
    ]
