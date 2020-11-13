# Generated by Django 3.1.2 on 2020-10-21 18:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=10)),
                ('capacity', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('identity_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buses.bus')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buses.driver')),
                ('journey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buses.journey')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.DateTimeField(default=django.utils.timezone.now)),
                ('arrival', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=5)),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buses.passenger')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buses.route')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='buses.schedule'),
        ),
    ]
