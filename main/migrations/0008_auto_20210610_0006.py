# Generated by Django 3.2.4 on 2021-06-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210609_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.ImageField(default='', upload_to='posts_media/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='user_avatar',
            field=models.ImageField(default='', upload_to='posts_media/', verbose_name='Аватар профиля'),
        ),
    ]
