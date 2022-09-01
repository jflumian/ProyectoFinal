# Generated by Django 4.1 on 2022-08-31 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_app', '0007_video_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='categorias',
            field=models.ManyToManyField(blank=True, null=True, related_name='imágenes', to='recursos_app.categoria'),
        ),
        migrations.AlterField(
            model_name='video',
            name='categorias',
            field=models.ManyToManyField(blank=True, null=True, related_name='videos', to='recursos_app.categoria'),
        ),
    ]