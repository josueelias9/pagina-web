# Generated by Django 3.0.5 on 2020-04-22 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('IE', models.CharField(max_length=200)),
                ('JP', models.CharField(max_length=200)),
                ('numero', models.IntegerField(default=0)),
            ],
        ),
    ]
