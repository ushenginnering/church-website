# Generated by Django 4.1.3 on 2022-12-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_videomessage_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklibrary',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videomessage',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]