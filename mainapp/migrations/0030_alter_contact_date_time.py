# Generated by Django 3.2 on 2022-09-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0029_alter_contact_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
