# Generated by Django 4.2.1 on 2024-11-05 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('llm_response', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
