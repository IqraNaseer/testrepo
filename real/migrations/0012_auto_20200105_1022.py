# Generated by Django 3.0 on 2020-01-05 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0011_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]