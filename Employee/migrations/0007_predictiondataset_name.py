# Generated by Django 4.0.3 on 2022-04-02 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0006_alter_predictiondataset_prediction'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictiondataset',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
