# Generated by Django 3.2.10 on 2022-09-02 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gettingApp', '0003_auto_20220902_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criminalprofil',
            options={'ordering': ['name']},
        ),
    ]