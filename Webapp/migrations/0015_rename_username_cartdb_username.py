# Generated by Django 5.0.4 on 2024-06-08 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0014_rename_username_cartdb_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdb',
            old_name='username',
            new_name='Username',
        ),
    ]