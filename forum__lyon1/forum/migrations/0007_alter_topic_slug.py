# Generated by Django 4.1.7 on 2023-04-01 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_alter_topic_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
