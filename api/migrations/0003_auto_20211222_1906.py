# Generated by Django 3.2.6 on 2021-12-22 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211222_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cofounder',
            old_name='desc_rus',
            new_name='desc_ru',
        ),
        migrations.RenameField(
            model_name='cofounder',
            old_name='full_name_rus',
            new_name='full_name_ru',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='desc_rus',
            new_name='desc_ru',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='title_rus',
            new_name='title_ru',
        ),
        migrations.RenameField(
            model_name='newscategory',
            old_name='type_rus',
            new_name='type_ru',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='desc_rus',
            new_name='desc_ru',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='text_rus',
            new_name='text_ru',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title_rus',
            new_name='title_ru',
        ),
        migrations.RenameField(
            model_name='shareholder',
            old_name='desc_rus',
            new_name='desc_ru',
        ),
        migrations.RenameField(
            model_name='shareholder',
            old_name='full_name_rus',
            new_name='full_name_ru',
        ),
    ]