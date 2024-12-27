# Generated by Django 5.1.4 on 2024-12-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('image', models.ImageField(upload_to='images/')),
                ('audio_file', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]
