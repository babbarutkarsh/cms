# Generated by Django 3.1.1 on 2020-11-07 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0008_auto_20201107_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alloted', models.BooleanField(default=False)),
                ('Management_Comments', models.TextField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='form',
            name='alloted',
            field=models.IntegerField(default=0),
        ),
    ]
