# Generated by Django 3.1.3 on 2020-11-04 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbours', '0002_remove_user_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='image',
            field=models.ImageField(default='noimage.png', upload_to='images/'),
        ),
    ]