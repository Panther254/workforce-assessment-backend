# Generated by Django 4.1.6 on 2023-02-06 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_date_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]