# Generated by Django 4.0.6 on 2022-10-04 02:52

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0005_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='medium',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('bangla', 'bangla'), ('english', 'english'), ('urdu', 'urdu'), ('hindi', 'hindi'), ('arabic', 'arabic')], default='bangla', max_length=100),
        ),
    ]
