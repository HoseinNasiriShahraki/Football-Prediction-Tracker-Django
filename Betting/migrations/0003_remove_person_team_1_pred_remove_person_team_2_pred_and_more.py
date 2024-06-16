# Generated by Django 5.0.6 on 2024-06-15 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Betting', '0002_person_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='Team_1_pred',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Team_2_pred',
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_1_pred', models.PositiveSmallIntegerField(verbose_name='Team 1 Prediction')),
                ('Team_2_pred', models.PositiveSmallIntegerField(verbose_name='Team 2 Prediction')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name+', to='Betting.person')),
            ],
            options={
                'verbose_name': 'Prediction',
                'verbose_name_plural': 'Predictions',
            },
        ),
    ]
