# Generated by Django 3.2.6 on 2022-05-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_shareholder_sequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='title_tr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
    ]