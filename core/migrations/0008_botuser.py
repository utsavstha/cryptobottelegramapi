# Generated by Django 4.1.7 on 2023-03-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_back_videomenu_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('language_code', models.CharField(max_length=50)),
                ('telegram_id', models.CharField(max_length=50)),
                ('registration_link', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'BotUser',
            },
        ),
    ]
