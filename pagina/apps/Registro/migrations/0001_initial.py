# Generated by Django 3.1.3 on 2020-11-11 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('anioPublicacion', models.IntegerField()),
                ('tipo', models.CharField(choices=[('Shounen', 'Shounen'), ('Shoujo', 'Shoujo'), ('Seinen', 'Seinen'), ('Josei', 'Josei')], max_length=50)),
                ('sinopsis', models.CharField(max_length=200)),
                ('fotografia', models.ImageField(blank=True, upload_to='catalogo_anime')),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('anioPublicacion', models.IntegerField()),
                ('estado', models.CharField(choices=[('Emision', 'Emision'), ('Finalizado', 'Finalizado')], max_length=50)),
                ('sinopsis', models.CharField(max_length=200)),
                ('fotografia', models.ImageField(blank=True, upload_to='catalogo_manga')),
            ],
        ),
    ]
