# Generated by Django 3.1.4 on 2020-12-14 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0003_auto_20201213_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mobileno',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
