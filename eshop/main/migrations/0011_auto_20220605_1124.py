# Generated by Django 3.2.12 on 2022-06-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20220605_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='beans',
            name='flavor1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='beans',
            name='flavor2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='beans',
            name='flavor3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='FlavorDetail',
        ),
    ]
