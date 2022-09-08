# Generated by Django 3.2.10 on 2022-09-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gettingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crime',
            options={'ordering': ['dateCondamnation']},
        ),
        migrations.AlterModelOptions(
            name='criminalprofil',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='crime',
            name='durePeine',
            field=models.IntegerField(blank=True, null=True, verbose_name='durée des peines(en mois)'),
        ),
        migrations.AlterField(
            model_name='criminalprofil',
            name='prenom',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='prenom'),
        ),
    ]
