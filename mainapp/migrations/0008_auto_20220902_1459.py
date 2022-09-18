# Generated by Django 3.2 on 2022-09-02 08:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20220902_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutusfirstsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='aboutus')),
            ],
            options={
                'verbose_name': 'First Section - About Page',
                'verbose_name_plural': 'First Section - About Page',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutuspagesubtitle',
            options={'verbose_name': 'Subtitle - About Page', 'verbose_name_plural': 'Subtitle - About Page'},
        ),
        migrations.AlterModelOptions(
            name='contactussection',
            options={'verbose_name': 'Contact-us - Homepage', 'verbose_name_plural': 'Contact-us - Homepage'},
        ),
        migrations.AlterModelOptions(
            name='footersection',
            options={'verbose_name': 'Footer - Homepage', 'verbose_name_plural': 'Footer - Homepage'},
        ),
        migrations.AlterModelOptions(
            name='headerhomepage',
            options={'verbose_name': 'Header - Homepage', 'verbose_name_plural': 'Header - Homepage'},
        ),
        migrations.AlterModelOptions(
            name='startupsection',
            options={'verbose_name': 'Startup - Homepage', 'verbose_name_plural': 'Startup - Homepage'},
        ),
        migrations.AlterModelOptions(
            name='testimonialsection',
            options={'verbose_name': 'Testimonial - Homepage', 'verbose_name_plural': 'Testimonial - Homepage'},
        ),
    ]