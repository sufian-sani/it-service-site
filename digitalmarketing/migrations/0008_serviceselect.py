# Generated by Django 3.2 on 2022-09-13 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0042_privacypolicybody_privacypolicypagesubtitle'),
        ('digitalmarketing', '0007_rename_productimage_portfolioimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serviceselect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceselect', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.servicesection')),
            ],
            options={
                'verbose_name': 'Service Select - SEO Page',
                'verbose_name_plural': 'Service Select - SEO Page',
            },
        ),
    ]
