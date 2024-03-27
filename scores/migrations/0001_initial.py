# Generated by Django 5.0.3 on 2024-03-27 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='targets',
            fields=[
                ('target_id', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('target_host', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Targets',
                'db_table': 'targets',
            },
        ),
        migrations.CreateModel(
            name='teams',
            fields=[
                ('team_id', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('points', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Teams',
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='ports',
            fields=[
                ('port_id', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('port_number', models.CharField(max_length=255)),
                ('service_name', models.CharField(max_length=255)),
                ('result_code', models.CharField(choices=[('SUC', 'success'), ('FAL', 'failure'), ('PAR', 'partial'), ('UNK', 'unknown'), ('ERR', 'error')], default='UNK', max_length=3)),
                ('participant_feedback', models.TextField()),
                ('staff_feedback', models.TextField()),
                ('points_obtained', models.IntegerField(default=0)),
                ('target_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scores.targets')),
            ],
            options={
                'verbose_name_plural': 'Ports',
                'db_table': 'ports',
            },
        ),
        migrations.AddField(
            model_name='targets',
            name='team_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scores.teams'),
        ),
    ]
