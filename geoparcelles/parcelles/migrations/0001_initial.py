# Generated by Django 5.2.2 on 2025-06-08 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('periode_semis', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parcelle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('culture', models.CharField(max_length=100)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('note', models.TextField()),
                ('parcelle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelles.parcelle')),
            ],
        ),
    ]
