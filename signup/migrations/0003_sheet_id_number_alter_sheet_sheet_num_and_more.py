# Generated by Django 4.1.1 on 2022-09-29 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_alter_sheet_end_date_alter_sheet_sheet_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheet',
            name='id_number',
            field=models.CharField(default=0, max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sheet_num',
            field=models.CharField(default='2', max_length=1),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
