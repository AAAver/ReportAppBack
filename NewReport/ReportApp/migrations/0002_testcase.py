# Generated by Django 3.1.3 on 2020-11-20 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReportApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('method_name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReportApp.run')),
            ],
        ),
    ]
