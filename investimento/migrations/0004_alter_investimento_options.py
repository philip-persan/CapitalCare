# Generated by Django 4.2.4 on 2023-10-01 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investimento', '0003_alter_tipoinvestimento_nome'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='investimento',
            options={'ordering': ['owner', '-data', 'tipo'], 'verbose_name': 'Investimento', 'verbose_name_plural': 'Investimentos'},
        ),
    ]