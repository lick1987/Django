# Generated by Django 2.1.7 on 2019-03-31 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20190331_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='user',
            new_name='userd',
        ),
    ]
