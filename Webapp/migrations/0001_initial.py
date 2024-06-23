# Generated by Django 5.0.4 on 2024-05-12 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Subject', models.CharField(blank=True, max_length=100, null=True)),
                ('Message', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]