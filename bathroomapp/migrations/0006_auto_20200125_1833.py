# Generated by Django 3.0.2 on 2020-01-25 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bathroomapp', '0005_auto_20200125_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bathroom',
            name='id',
        ),
        migrations.RemoveField(
            model_name='bathroom',
            name='ratingClean',
        ),
        migrations.RemoveField(
            model_name='bathroom',
            name='ratingConv',
        ),
        migrations.AlterField(
            model_name='bathroom',
            name='bathroomId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
