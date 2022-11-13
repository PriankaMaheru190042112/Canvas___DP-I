# Generated by Django 4.1.3 on 2022-11-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0029_remove_event_fee_remove_event_frame_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='frame_height',
            field=models.IntegerField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='frame_width',
            field=models.IntegerField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]