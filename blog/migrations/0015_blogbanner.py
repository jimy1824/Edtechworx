# Generated by Django 2.1.2 on 2018-10-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20181030_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('background_image', models.ImageField(blank=True, upload_to='background_imgs/')),
            ],
        ),
    ]