# Generated by Django 4.1.1 on 2022-09-29 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_sheet_id_number_alter_sheet_sheet_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='sheet_num',
            field=models.CharField(default='4', max_length=1),
        ),
    ]
