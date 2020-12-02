# Generated by Django 3.1.3 on 2020-11-24 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReportApp', '0006_auto_20201124_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='run_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='testresult',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='ReportApp.run'),
        ),
    ]