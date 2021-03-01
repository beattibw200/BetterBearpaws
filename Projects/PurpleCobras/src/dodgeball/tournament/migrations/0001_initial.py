# Generated by Django 3.1.6 on 2021-02-22 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_of', models.DateField(help_text='Date')),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-completed', 'date_of'],
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_index', models.IntegerField()),
                ('winner', models.CharField(choices=[('1', 'Team 1'), ('2', 'Team 2'), ('-', 'None')], default='-', help_text='Winner', max_length=1)),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_1_matches', related_query_name='team_1_match', to='tournament.team')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team_2_matches', related_query_name='team_2_match', to='tournament.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament')),
            ],
        ),
    ]