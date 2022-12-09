# Generated by Django 4.1.3 on 2022-12-05 12:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_booklibrary_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrayerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='First name')),
                ('lastname', models.CharField(max_length=50, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('request', models.CharField(max_length=2000, verbose_name='Prayer Request')),
            ],
        ),
        migrations.AlterField(
            model_name='booklibrary',
            name='cover_page',
            field=models.ImageField(upload_to='BookLibrary/CoverPage'),
        ),
    ]