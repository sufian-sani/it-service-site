# Generated by Django 3.2 on 2022-09-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0050_servicepagemeta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Startuppagemeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=200)),
                ('meta_description', models.CharField(max_length=500)),
                ('meta_keywords', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Startup Meta - Start up Page',
                'verbose_name_plural': 'Startup Meta - Start up Page',
            },
        ),
        migrations.AlterModelOptions(
            name='servicepagemeta',
            options={'verbose_name': 'Service Meta - Service Page', 'verbose_name_plural': 'Service Meta - Service Page'},
        ),
    ]
