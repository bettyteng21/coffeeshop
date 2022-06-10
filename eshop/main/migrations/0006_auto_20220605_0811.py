# Generated by Django 3.2.12 on 2022-06-05 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220605_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavor',
            name='beans',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.beans'),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='flavor',
            field=models.CharField(max_length=100, null=True),
        ),
    ]