# Generated by Django 4.1.1 on 2022-09-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('num_bedrooms', models.IntegerField()),
                ('num_bathrooms', models.IntegerField()),
                ('square_footage', models.IntegerField()),
                ('adress', models.CharField(max_length=350)),
            ],
        ),
    ]
