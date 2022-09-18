# Generated by Django 3.2 on 2022-09-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_teampagesubtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teampage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='teampage')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Team - Team Page',
                'verbose_name_plural': 'Team - Team Page',
            },
        ),
    ]
