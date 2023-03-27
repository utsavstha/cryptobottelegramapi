# Generated by Django 4.1.7 on 2023-03-27 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot_name', models.CharField(max_length=100)),
                ('bot_language', models.CharField(choices=[('English', 'en'), ('Spanish', 'es')], default='English', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('file', models.FileField(blank=True, upload_to='files')),
                ('continue_to_main_menu', models.CharField(max_length=50)),
                ('bot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.bot')),
            ],
            options={
                'verbose_name_plural': 'Welcome',
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name_seller', models.CharField(max_length=100)),
                ('seller_whatsapp_number', models.CharField(max_length=50)),
                ('seller_referral_link', models.CharField(max_length=50)),
                ('telegram_bot_url', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('bot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Bot', to='core.bot')),
            ],
        ),
    ]