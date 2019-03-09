# Generated by Django 2.1.7 on 2019-03-09 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20190309_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='diagnosis',
        ),
        migrations.AddField(
            model_name='student',
            name='code',
            field=models.CharField(blank=True, choices=[('ADHD', 'Attention-Deficit/Hyperactivity Disorder'), ('ASD', 'Autism Spectrum Disorder'), ('BI1', 'Brain Injury Level 1'), ('BI2', 'Brain Injury Level 2'), ('BI3', 'Brain Injury Level 3'), ('DS', 'Down Syndrome'), ('EDBS', 'Emotional/Behavioral Disorder'), ('GD', 'Global Delay'), ('LD', 'Learning Delay'), ('PDD', 'Pervasive Developmental Disorder')], max_length=4),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]