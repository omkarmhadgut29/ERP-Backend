# Generated by Django 4.0.3 on 2022-04-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_customerpredictiondataset'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerpredictiondataset',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]