# Generated by Django 2.1.7 on 2019-03-31 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='uemail',
        ),
    ]
