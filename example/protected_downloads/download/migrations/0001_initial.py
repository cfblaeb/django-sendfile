# Generated by Django 4.1.1 on 2022-09-21 18:46

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_public', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=pathlib.PurePosixPath('/home/laeb/PycharmProjects/django-sendfile/examples/protected_downloads/protected')), upload_to='download')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
