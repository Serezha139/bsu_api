# Generated by Django 2.1.3 on 2018-11-13 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20181107_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]