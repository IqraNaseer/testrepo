# Generated by Django 3.0 on 2020-01-05 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0014_inquiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='nam_c',
        ),
        migrations.RenameField(
            model_name='inquiry',
            old_name='name',
            new_name='name_i',
        ),
    ]
