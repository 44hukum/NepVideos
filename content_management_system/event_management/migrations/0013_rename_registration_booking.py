# Generated by Django 4.2.5 on 2023-09-17 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0012_alter_event_feature_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registration',
            new_name='Booking',
        ),
    ]
