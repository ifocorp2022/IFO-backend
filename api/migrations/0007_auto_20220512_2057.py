# Generated by Django 3.2.6 on 2022-05-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220512_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='desc_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='desc_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='desc_tr',
            field=models.TextField(blank=True, null=True),
        ),
    ]
