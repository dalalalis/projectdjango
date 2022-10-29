# Generated by Django 4.1.2 on 2022-10-29 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisers', '0005_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='organisers.booking'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='seatbooked',
            field=models.IntegerField(),
        ),
    ]
