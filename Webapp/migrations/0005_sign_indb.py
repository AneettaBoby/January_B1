# Generated by Django 5.0.4 on 2024-06-02 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0004_alter_register_db_confirm_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign_InDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
                ('Confirm_password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
