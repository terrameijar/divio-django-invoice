# Generated by Django 2.2.10 on 2020-03-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='company_logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
