# Generated by Django 4.2.10 on 2024-02-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('ingredients', models.CharField(help_text='seperated by a comma', max_length=300)),
                ('cooking_time', models.FloatField(help_text='in minutes')),
            ],
        ),
    ]
