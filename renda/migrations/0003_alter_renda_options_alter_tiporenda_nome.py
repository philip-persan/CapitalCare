# Generated by Django 4.2.4 on 2023-09-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renda', '0002_alter_renda_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='renda',
            options={'ordering': ['owner', 'tipo', '-data'], 'verbose_name': 'Renda', 'verbose_name_plural': 'Rendas'},
        ),
        migrations.AlterField(
            model_name='tiporenda',
            name='nome',
            field=models.CharField(default='Salário', max_length=50, verbose_name='Nome'),
        ),
    ]