# Generated by Django 2.1.1 on 2018-10-25 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('starting_date', models.DateTimeField()),
                ('ending_date', models.DateTimeField()),
                ('ticket_price', models.IntegerField()),
                ('place', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('organizing_company', models.CharField(max_length=500)),
                ('company_address', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='profile_images/')),
                ('fb_link', models.CharField(blank=True, max_length=500)),
                ('twiter_link', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
