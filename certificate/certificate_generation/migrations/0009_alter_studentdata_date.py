# Generated by Django 4.2.6 on 2023-10-22 17:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_generation', '0008_alter_studentdata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]