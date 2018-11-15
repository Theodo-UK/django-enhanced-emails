# Generated by Django 2.1.3 on 2018-11-18 22:12

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SentEmail',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('to', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), size=None)),
                ('cc', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), size=None)),
                ('bcc', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), size=None)),
            ],
            options={
                'ordering': ('-sent_at',),
                'get_latest_by': 'sent_at',
            },
        ),
    ]