# Generated by Django 4.1.6 on 2023-02-08 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_jobapplication_phone_number_jobapplication_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_logo',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='resume',
        ),
        migrations.AddField(
            model_name='job',
            name='company_logo_url',
            field=models.URLField(default='logo.png', max_length=300),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='resume_link',
            field=models.URLField(default='logo.png'),
        ),
    ]
