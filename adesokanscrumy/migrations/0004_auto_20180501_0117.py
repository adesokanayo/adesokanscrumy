# Generated by Django 2.0.4 on 2018-05-01 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adesokanscrumy', '0003_auto_20180501_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalstatus',
            name='category',
            field=models.CharField(choices=[('1', 'Verify'), ('2', 'Done'), ('3', 'Weekly Target'), ('4', 'Daily Target')], max_length=100),
        ),
    ]
