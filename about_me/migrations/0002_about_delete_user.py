# Generated by Django 5.1.5 on 2025-02-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('resume_link', models.FileField(upload_to='resume')),
            ],
            options={
                'verbose_name_plural': 'About sahifasi',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
