# Generated by Django 4.0.3 on 2022-12-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('song_name', models.CharField(max_length=300, unique=True)),
                ('image', models.ImageField(upload_to='image')),
                ('song', models.FileField(upload_to='audio')),
            ],
        ),
    ]
