# Generated by Django 4.0.3 on 2022-04-10 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_remove_user_uploaddate_item_uploaddate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='item',
            new_name='itemId',
        ),
    ]
