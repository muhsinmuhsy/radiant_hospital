# Generated by Django 5.1.4 on 2025-01-13 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_speciality_benefits'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='category',
            new_name='categories',
        ),
    ]
