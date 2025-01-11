# Generated by Django 5.1.4 on 2025-01-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_name_serviceheader_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='services/'),
        ),
    ]
