# Generated by Django 5.0.4 on 2024-06-12 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0015_rename_username_cartdb_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Address', models.EmailField(blank=True, max_length=100, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
