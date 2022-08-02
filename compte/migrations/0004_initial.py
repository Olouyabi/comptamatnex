# Generated by Django 4.0.3 on 2022-08-02 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compte', '0003_delete_membreuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembreUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True, verbose_name="Nom d'utilisateur")),
                ('first_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Prénom')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Prénom')),
                ('password', models.CharField(max_length=20, null=True, verbose_name='Mot de passe')),
                ('shipping_id', models.CharField(max_length=20, null=True, verbose_name='Code de livraison')),
                ('bio', models.TextField(default="Aucun bio n'est disponible...")),
                ('avatar', models.ImageField(default='assets/imgs-blog/avatar-defualt.jpg', upload_to='members')),
            ],
            options={
                'verbose_name': 'Membre',
            },
        ),
    ]
