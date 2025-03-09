# Generated by Django 5.1.4 on 2025-03-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_consultant_available_days_consultant_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciality',
            name='category',
            field=models.CharField(blank=True, choices=[('Surgical Procedures', 'Surgical Procedures'), ('Endoscopic Procedures', 'Endoscopic Procedures')], max_length=255, null=True),
        ),
    ]
