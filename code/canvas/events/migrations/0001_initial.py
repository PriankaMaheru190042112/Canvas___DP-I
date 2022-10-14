# Generated by Django 3.0.5 on 2022-09-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('type', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('photos_added', models.IntegerField(default=0, max_length=1)),
            ],
        ),
    ]