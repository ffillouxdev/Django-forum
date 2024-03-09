# Generated by Django 4.1.7 on 2023-04-01 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_follows_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='follows',
        ),
        migrations.AddField(
            model_name='user',
            name='studies',
            field=models.CharField(choices=[('IT license', 'IT license'), ('MATH license', 'MATH license'), ('PHYS license', 'PHYS license'), ('Medecine', 'Medecine'), ('Sociology license', 'Sociology license')], default=None, max_length=30, verbose_name='Studies'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('professor', 'Professor'), ('student', 'Student')], max_length=30, verbose_name='Rôle'),
        ),
    ]