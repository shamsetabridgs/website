# Generated by Django 4.0.6 on 2022-10-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0004_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.png', upload_to='tuition/images'),
        ),
    ]
