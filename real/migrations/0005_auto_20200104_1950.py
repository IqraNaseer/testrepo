# Generated by Django 3.0 on 2020-01-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0004_auto_20200104_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='name',
            field=models.CharField(default='', max_length=90),
        ),
    ]