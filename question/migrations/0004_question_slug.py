# Generated by Django 3.1.1 on 2020-09-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20200928_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default=None, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
