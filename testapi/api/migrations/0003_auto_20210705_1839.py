# Generated by Django 3.1.7 on 2021-07-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='iin',
            field=models.IntegerField(max_length=200),
        ),
    ]
