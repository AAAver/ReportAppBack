# Generated by Django 3.1.3 on 2020-12-01 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReportApp', '0012_run_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='project',
        ),
    ]
