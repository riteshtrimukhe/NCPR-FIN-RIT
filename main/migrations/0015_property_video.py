# Generated by Django 5.0.7 on 2024-08-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_property_price2'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='video',
            field=models.TextField(null=True),
        ),
    ]
