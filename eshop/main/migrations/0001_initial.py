# Generated by Django 3.2.12 on 2022-06-04 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(default=0)),
                ('picture', models.URLField()),
                ('description', models.TextField()),
                ('origin', models.CharField(max_length=100)),
                ('roast', models.CharField(choices=[('L', 'Light'), ('M', 'Medium'), ('D', 'Dark')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='FlavorDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.CharField(max_length=100)),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.beans')),
            ],
        ),
    ]
