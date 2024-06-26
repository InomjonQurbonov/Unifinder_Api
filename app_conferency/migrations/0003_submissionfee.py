# Generated by Django 5.0.6 on 2024-06-12 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_conferency', '0002_conferencyagenda_conferencysections_partners'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_for', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_price', models.FloatField(blank=True, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_description', models.TextField(blank=True, null=True)),
                ('conferency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_conferency.conferency')),
            ],
            options={
                'verbose_name': 'Submission Fee',
                'verbose_name_plural': 'Submission Fee',
                'db_table': 'submission_fee',
            },
        ),
    ]
