# Generated by Django 2.2.4 on 2020-08-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200808_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='tenure_types',
            field=models.IntegerField(choices=[(1, 'Years'), (2, 'Months'), (3, 'Weeks')], db_index=True, default=1),
        ),
    ]