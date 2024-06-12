# Generated by Django 5.0.6 on 2024-06-12 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_users.user')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Author',
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_title', models.CharField(blank=True, max_length=255, null=True)),
                ('paper_section', models.CharField(blank=True, max_length=255, null=True)),
                ('paper_tegs', models.CharField(blank=True, max_length=255, null=True)),
                ('paper_file', models.FileField(blank=True, null=True, upload_to='papers')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_users.author')),
            ],
        ),
    ]