# Generated by Django 4.1.7 on 2023-04-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_topic_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='section',
            field=models.CharField(choices=[('IT section', 'IT section'), ('MATH section', 'MATH section'), ('PHYS section', 'PHYS section'), ('Medecine section', 'Medecine section'), ('Sociology section', 'Sociology section')], default='None', max_length=30, verbose_name='Section'),
        ),
    ]
