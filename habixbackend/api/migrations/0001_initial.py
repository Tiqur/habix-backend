# Generated by Django 3.1.4 on 2021-01-03 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HabixUser',
            fields=[
                ('uuid', models.BigIntegerField(max_length=20, primary_key=True, serialize=False)),
                ('timezone', models.IntegerField(verbose_name='UTC offset')),
            ],
        ),
        migrations.CreateModel(
            name='DailyTasks',
            fields=[
                ('habixuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.habixuser')),
                ('task_name', models.CharField(max_length=200)),
                ('streak_graph', models.CharField(max_length=50000)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('best_streak', models.PositiveIntegerField(default=0)),
            ],
            bases=('api.habixuser',),
        ),
    ]
