# Generated by Django 2.1.2 on 2018-10-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_courseoutline'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('posting_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='comments',
            field=models.ManyToManyField(to='courses.CourseComments'),
        ),
    ]