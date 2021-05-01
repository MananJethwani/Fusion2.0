# Generated by Django 3.1.5 on 2021-04-25 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0003_auto_20191024_1242'),
        ('ps1', '0004_auto_20210421_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockentry',
            name='dealing_assistant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo'),
        ),
        migrations.AlterField(
            model_name='stockentry',
            name='item_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ps1.indentfile'),
        ),
    ]
