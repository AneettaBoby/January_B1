# Generated by Django 5.0.4 on 2024-06-05 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0008_rename_email_cartdb_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_db',
            old_name='UserName',
            new_name='Username',
        ),
    ]
