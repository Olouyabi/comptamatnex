# Generated by Django 4.0.3 on 2022-08-02 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0002_remove_membreuser_code_livre'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MembreUser',
        ),
    ]
