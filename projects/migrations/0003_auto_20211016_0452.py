# Generated by Django 3.2.8 on 2021-10-15 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211016_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]