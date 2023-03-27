# Generated by Django 4.1.7 on 2023-03-27 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_welcome_file_alter_bot_bot_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('presentation_pdf', models.CharField(max_length=50)),
                ('presentation_videos', models.CharField(max_length=50)),
                ('register', models.CharField(max_length=50)),
                ('bot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.bot')),
            ],
            options={
                'verbose_name_plural': 'MainMenu',
            },
        ),
    ]
