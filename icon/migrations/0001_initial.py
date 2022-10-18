# Generated by Django 3.2.12 on 2022-05-14 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('display_name', models.CharField(max_length=255)),
                ('display_image', models.ImageField(blank=True, null=True, upload_to='icon_logos')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IconTeam',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.EmailField(max_length=254)),
                ('updated_by', models.EmailField(max_length=254)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('team_name', models.CharField(max_length=255, verbose_name='Team name')),
                ('display_image', models.ImageField(blank=True, null=True, upload_to='team_logos')),
                ('icon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='icon.icon')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IconTeamMember',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('joined_at', models.DateTimeField()),
                ('left_at', models.DateTimeField(blank=True, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icon.iconteam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
