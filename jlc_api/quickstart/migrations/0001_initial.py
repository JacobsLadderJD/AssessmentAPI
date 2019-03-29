# Generated by Django 2.1.7 on 2019-03-29 05:24

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import jlc_api.quickstart.json_defaults


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField()),
                ('editedAt', models.DateField()),
                ('notesSection', django.contrib.postgres.fields.jsonb.JSONField(default=jlc_api.quickstart.json_defaults.notes_blank, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('reflexSection', django.contrib.postgres.fields.jsonb.JSONField(default=jlc_api.quickstart.json_defaults.reflex_blank, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('tactilitySection', django.contrib.postgres.fields.jsonb.JSONField(default=jlc_api.quickstart.json_defaults.tactility_blank, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('auditorySection', django.contrib.postgres.fields.jsonb.JSONField(default=jlc_api.quickstart.json_defaults.auditory_blank, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('visualSection', django.contrib.postgres.fields.jsonb.JSONField(default=jlc_api.quickstart.json_defaults.visual_blank, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('manualSection', django.contrib.postgres.fields.jsonb.JSONField(default=jlc_api.quickstart.json_defaults.manual_blank, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('languageSection', django.contrib.postgres.fields.jsonb.JSONField(default=jlc_api.quickstart.json_defaults.language_blank, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('mobilitySection', django.contrib.postgres.fields.jsonb.JSONField(default=jlc_api.quickstart.json_defaults.mobility_blank, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('sensorySection', django.contrib.postgres.fields.jsonb.JSONField(default=jlc_api.quickstart.json_defaults.sensory_blank, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('sensitivitiesSection', django.contrib.postgres.fields.jsonb.JSONField(default=jlc_api.quickstart.json_defaults.sensitivities_blank, encoder=django.core.serializers.json.DjangoJSONEncoder)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, choices=[('ADHD', 'Attention-Deficit/Hyperactivity Disorder'), ('ASD', 'Autism Spectrum Disorder'), ('BI1', 'Brain Injury Level 1'), ('BI2', 'Brain Injury Level 2'), ('BI3', 'Brain Injury Level 3'), ('DS', 'Down Syndrome'), ('EDBS', 'Emotional/Behavioral Disorder'), ('GD', 'Global Delay'), ('LD', 'Learning Delay'), ('PDD', 'Pervasive Developmental Disorder')], max_length=4)),
                ('status', models.CharField(max_length=20)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='evaluation',
            name='evaluatorId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.Evaluator'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='studentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.Student'),
        ),
    ]
