# Generated by Django 5.1.2 on 2024-11-05 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_management', '0002_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('ACCEPTED', 'Accepted'), ('PENDING', 'Pending')], default='PENDING', max_length=20),
        ),
    ]