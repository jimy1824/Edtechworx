# Generated by Django 2.1.2 on 2018-10-30 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_companyabouts'),
        ('blog', '0009_remove_blogs_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='author',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='about.Team'),
        ),
    ]
