# Generated by Django 3.2.6 on 2022-05-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_timeline_increment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothingSliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sliders/', verbose_name='Enter img url')),
            ],
            options={
                'verbose_name': 'ClothingSliderImage',
                'verbose_name_plural': 'ClothingSliderImages',
            },
        ),
        migrations.CreateModel(
            name='CompanySliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sliders/', verbose_name='Enter img url')),
            ],
            options={
                'verbose_name': 'CompanySliderImage',
                'verbose_name_plural': 'CompanySliderImages',
            },
        ),
        migrations.CreateModel(
            name='CreativeSliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sliders/', verbose_name='Enter img url')),
            ],
            options={
                'verbose_name': 'CreativeSliderImage',
                'verbose_name_plural': 'CreativeSliderImages',
            },
        ),
        migrations.CreateModel(
            name='CreativeSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ManyToManyField(to='api.CreativeSliderImage')),
            ],
            options={
                'verbose_name': 'CreativeSlider',
                'verbose_name_plural': 'CreativeSliders',
            },
        ),
        migrations.CreateModel(
            name='CompanySlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ManyToManyField(to='api.CompanySliderImage')),
            ],
            options={
                'verbose_name': 'CompanySlider',
                'verbose_name_plural': 'CompanySliders',
            },
        ),
        migrations.CreateModel(
            name='ClothingSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ManyToManyField(to='api.ClothingSliderImage')),
            ],
            options={
                'verbose_name': 'ClothingSlider',
                'verbose_name_plural': 'ClothingSliders',
            },
        ),
    ]