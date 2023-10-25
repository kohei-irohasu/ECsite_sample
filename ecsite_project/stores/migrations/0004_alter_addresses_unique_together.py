# Generated by Django 4.2.6 on 2023-10-24 23:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0003_addresses'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='addresses',
            unique_together={('zip_code', 'prefecture', 'address', 'user')},
        ),
    ]
