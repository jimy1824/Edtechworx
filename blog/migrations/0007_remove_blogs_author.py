# Generated by Django 2.1.2 on 2018-10-30 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181030_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='author',
        ),
    ]
