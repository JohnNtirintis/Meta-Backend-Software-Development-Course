# Generated by Django 4.2.5 on 2023-09-11 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
