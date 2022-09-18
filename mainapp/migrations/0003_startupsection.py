# Generated by Django 3.2 on 2022-08-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_header_homepage_headerhomepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Startupsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='startup_section')),
            ],
            options={
                'verbose_name': 'Startup Section',
                'verbose_name_plural': 'Startup Section',
            },
        ),
    ]
