# Generated by Django 4.1.7 on 2023-04-01 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_section_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='section',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='forum.section'),
        ),
    ]
