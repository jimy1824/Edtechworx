# Generated by Django 2.1.1 on 2018-10-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20181029_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('background_image', models.ImageField(blank=True, upload_to='background_imgs/')),
            ],
        ),
    ]
