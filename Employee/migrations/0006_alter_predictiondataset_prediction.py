# Generated by Django 4.0.3 on 2022-03-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0005_predictiondataset_prediction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictiondataset',
            name='prediction',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
