# Generated by Django 5.0.3 on 2024-03-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.URLField(max_length=50, unique=True),
        ),
    ]