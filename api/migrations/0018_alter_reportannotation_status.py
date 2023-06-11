# Generated by Django 4.1.3 on 2023-05-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_report_category_2_alter_report_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportannotation',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'RS_STATUS_NONE'), (1, 'RS_REPORTED'), (2, 'RS_CLASSIFIED'), (3, 'RS_REPORTED_TO_AUTHORITIES'), (4, 'RS_NOT_RELEVANT'), (5, 'RS_REPORT_IN_PROGRESS'), (6, 'RS_SOLVED'), (7, 'RS_CHECK_ON_THE_FIELD')], default=1, null=True),
        ),
    ]
