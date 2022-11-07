# Generated by Django 4.1.3 on 2022-11-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('experience_years', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
    ]