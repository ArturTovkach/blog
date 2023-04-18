# Generated by Django 3.2.18 on 2023-04-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230414_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='choice',
            field=models.CharField(choices=[('male', 'Мужской род'), ('female', 'Женский пол')], default='male', max_length=6, verbose_name='Выберите пол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.png', upload_to='user_images', verbose_name='Фото пользователя'),
        ),
    ]