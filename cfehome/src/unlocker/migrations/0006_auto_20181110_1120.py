# Generated by Django 2.0.9 on 2018-11-10 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlocker', '0005_auto_20181109_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetimerequest',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]
