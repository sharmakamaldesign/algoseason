# Generated by Django 3.1.1 on 2021-06-24 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0027_auto_20210624_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='syllabus',
            old_name='syllabusType',
            new_name='syllabus_type',
        ),
    ]
