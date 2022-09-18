# Generated by Django 3.2 on 2022-09-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(blank=True, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact - Contactus Page',
                'verbose_name_plural': 'Contact - Contactus Page',
            },
        ),
    ]