# Generated by Django 4.1.3 on 2022-12-02 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videomessage',
            name='description',
        ),
        migrations.AlterField(
            model_name='booklibrary',
            name='short_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='videomessage',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
