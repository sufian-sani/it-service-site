# Generated by Django 3.2 on 2022-09-12 19:20

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0041_pricingsubscribe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privacypolicybody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Body Description - Privacy Policy Page',
                'verbose_name_plural': 'Body Description - Privacy Policy Page',
            },
        ),
        migrations.CreateModel(
            name='Privacypolicypagesubtitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Subtitle - Privacy Policy Page',
                'verbose_name_plural': 'Subtitle - Privacy Policy Page',
            },
        ),
    ]
