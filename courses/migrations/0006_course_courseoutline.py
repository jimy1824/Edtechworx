# Generated by Django 2.1.2 on 2018-10-30 13:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_course_courseoutline'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseoutline',
            field=ckeditor.fields.RichTextField(default='jkskdkf'),
            preserve_default=False,
        ),
    ]
