# Generated by Django 4.1.7 on 2023-03-27 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_videomenuoption_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videomenu',
            old_name='back',
            new_name='register',
        ),
    ]