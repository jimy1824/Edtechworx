# Generated by Django 2.1.2 on 2018-10-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_blogs_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomments',
            name='posting_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]