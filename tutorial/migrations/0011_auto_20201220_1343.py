# Generated by Django 3.1.1 on 2020-12-20 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0010_auto_20201130_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyllabusSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('index', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.syllabuscategory')),
            ],
        ),
        migrations.AddField(
            model_name='syllabus',
            name='subCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutorial.syllabussubcategory'),
            preserve_default=False,
        ),
    ]
