# Generated by Django 3.1.3 on 2020-11-21 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReportApp', '0003_auto_20201121_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewTestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(max_length=4000)),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReportApp.run')),
            ],
        ),
    ]
