# Generated by Django 3.2.12 on 2022-06-05 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220605_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flavordetail',
            name='beans',
        ),
        migrations.AddField(
            model_name='flavordetail',
            name='beans',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.beans'),
        ),
    ]
