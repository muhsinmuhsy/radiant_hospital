# Generated by Django 5.1.4 on 2025-01-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_blog_category_alter_mission_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='benefits',
            field=models.JSONField(default=list),
        ),
    ]
