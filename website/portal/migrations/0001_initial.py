# Generated by Django 4.2.2 on 2023-06-22 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=200)),
                ('seat_type', models.BooleanField()),
                ('quota', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('opening_rank', models.PositiveIntegerField(default=200000)),
                ('closing_rank', models.PositiveIntegerField(default=200000)),
                ('year', models.PositiveSmallIntegerField(default=2022)),
                ('round', models.PositiveSmallIntegerField(default=6)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mains_rank', models.IntegerField()),
                ('advanced_rank', models.IntegerField()),
                ('seat_type', models.BooleanField()),
                ('quota', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
    ]
