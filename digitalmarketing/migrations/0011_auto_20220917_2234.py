# Generated by Django 3.2 on 2022-09-17 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalmarketing', '0010_seoservicehomepage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Seoservicehomepage',
            new_name='Seoservicehomepagemeta',
        ),
        migrations.AlterModelOptions(
            name='seoservicehomepagemeta',
            options={'verbose_name': 'SEO Service Page Meta - SEO Homepage', 'verbose_name_plural': 'SEO Service Page Meta - SEO Homepage'},
        ),
    ]
