# Generated by Django 4.2.15 on 2024-08-20 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImgApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('card_title', models.CharField(max_length=50)),
                ('card_description', models.CharField(max_length=1000)),
            ],
        ),
    ]
