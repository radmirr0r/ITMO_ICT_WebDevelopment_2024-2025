# Generated by Django 5.1.7 on 2025-03-21 14:10

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('publishing_year', models.DateField()),
                ('cipher', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Copy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.book')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('passport', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=11)),
                ('education', models.CharField(choices=[('0', 'no education'), ('1', 'elementary'), ('2', 'middle'), ('3', 'bachelor'), ('4', 'master')], default='0', max_length=1)),
                ('phd', models.BooleanField()),
                ('library_card_number', models.CharField(max_length=10)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.hall')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField(default=django.utils.timezone.now)),
                ('date_returned', models.DateField(blank=True, default=None, null=True)),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.copy')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.reader')),
            ],
        ),
    ]
