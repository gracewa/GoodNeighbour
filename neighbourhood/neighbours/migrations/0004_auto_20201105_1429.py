# Generated by Django 3.1.3 on 2020-11-05 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbours', '0003_neighbourhood_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
