# Generated by Django 3.2.10 on 2022-09-08 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gettingApp', '0004_alter_criminalprofil_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminalprofil',
            name='adresse',
            field=models.CharField(blank=True, default='30 av. lufira v.Paris', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='criminalprofil',
            name='etatcivile',
            field=models.CharField(blank=True, choices=[('marié', 'marié'), ('célibataire', 'célibataire'), ('divorcé', 'divorcé'), ('veuve ou veuf', 'veuve ou veuf')], max_length=30, null=True, verbose_name='Etat civil'),
        ),
        migrations.AlterField(
            model_name='crime',
            name='organeCondamnatoire',
            field=models.CharField(blank=True, default='cours de venise', max_length=100, null=True, verbose_name='cours ou tribunaux'),
        ),
    ]