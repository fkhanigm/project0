# Generated by Django 3.0.5 on 2020-04-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200421_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_image',
            field=models.ImageField(null=True, upload_to='static/pic'),
        ),
    ]