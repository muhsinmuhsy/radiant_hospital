# Generated by Django 5.1.4 on 2025-01-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_consultantheader'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialitiesHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='WeProvideItem',
            new_name='Specialities',
        ),
    ]
