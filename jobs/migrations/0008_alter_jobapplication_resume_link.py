# Generated by Django 4.1.6 on 2023-02-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_job_company_logo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='resume_link',
            field=models.URLField(default=''),
        ),
    ]
