# Generated by Django 3.0 on 2020-01-05 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0012_auto_20200105_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=70),
        ),
    ]
