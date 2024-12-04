# Generated by Django 5.1.2 on 2024-11-16 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='property_images/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
