# Generated by Django 2.2.6 on 2019-10-07 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_id', models.CharField(max_length=30)),
                ('machine_number', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
