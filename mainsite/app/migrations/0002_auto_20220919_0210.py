# Generated by Django 3.2.12 on 2022-09-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.IntegerField(null=None),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.FloatField(null=None),
        ),
        migrations.AlterField(
            model_name='food',
            name='fats',
            field=models.FloatField(null=None),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.FloatField(null=None),
        ),
    ]