
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(upload_to='', verbose_name='Photo de profil'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CREATOR', 'Createur'), ('SUBSCRIBER', 'Abonné')], max_length=30, verbose_name='Rôle'),
        ),
    ]
