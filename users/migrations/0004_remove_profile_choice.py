# Generated by Django 3.2.18 on 2023-04-18 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230415_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='choice',
        ),
    ]