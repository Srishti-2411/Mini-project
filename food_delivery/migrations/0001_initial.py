# Generated by Django 3.2.4 on 2022-01-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('psw', models.CharField(max_length=10)),
                ('pswr', models.CharField(max_length=10)),
            ],
        ),
    ]
