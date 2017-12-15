# Generated by Django 2.0 on 2017-12-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RGs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Capability', models.CharField(max_length=140)),
                ('Capability_Status', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RG', models.CharField(max_length=140)),
            ],
        ),
    ]
