# Generated by Django 3.1.1 on 2020-09-18 07:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0003_job_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]