# Generated by Django 3.2.12 on 2022-06-05 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220605_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavordetail',
            name='beans',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.beans'),
        ),
        migrations.AddField(
            model_name='flavordetail',
            name='flavor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='flavordetail',
            name='detail',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Flavor',
        ),
    ]