# Generated by Django 2.0.3 on 2018-03-14 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrecipEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('month', models.CharField(blank=True, choices=[['JAN', 'JAN'], ['FEB', 'FEB'], ['MAR', 'MAR'], ['APR', 'APR'], ['MAY', 'MAY'], ['JUN', 'JUN'], ['JUL', 'JUL'], ['AUG', 'AUG'], ['SEP', 'SEP'], ['OCT', 'OCT'], ['NOV', 'NOV'], ['DEC', 'DEC']], max_length=3, null=True)),
                ('precip', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Precip Event',
            },
        ),
        migrations.CreateModel(
            name='Raingage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=150, unique=True)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=5, max_digits=15, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Raingage',
            },
        ),
        migrations.AddField(
            model_name='precipevent',
            name='raingage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='precip_events', to='appsrer.Raingage'),
        ),
    ]
