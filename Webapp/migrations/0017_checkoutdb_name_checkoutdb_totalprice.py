# Generated by Django 5.0.4 on 2024-06-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0016_checkoutdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutdb',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='checkoutdb',
            name='Totalprice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]