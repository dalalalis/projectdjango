# Generated by Django 4.1.2 on 2022-10-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventitem',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
