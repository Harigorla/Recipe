# Generated by Django 2.0 on 2020-11-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ename', models.CharField(max_length=200)),
                ('Eid', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
