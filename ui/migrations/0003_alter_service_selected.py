# Generated by Django 4.1.4 on 2023-05-04 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0002_alter_service_data_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='selected',
            field=models.CharField(max_length=50, verbose_name='selected'),
        ),
    ]
