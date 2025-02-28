# Generated by Django 4.0.6 on 2022-08-15 22:18

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_migrate_category_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='category_2',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('NONE_CAT_2', 'NONE_CAT_2'), ('LANE_HOLE', 'LANE_HOLE'), ('LANE_POOR_CONDITION', 'LANE_POOR_CONDITION'), ('LANE_VANISHED_PAINT', 'LANE_VANISHED_PAINT'), ('LANE_UNCLEAR_SIGNAGE', 'LANE_UNCLEAR_SIGNAGE'), ('LANE_BORDER_NEED_TO_BE_LOWERED', 'LANE_BORDER_NEED_TO_BE_LOWERED'), ('LANE_SLIPPERY', 'LANE_SLIPPERY'), ('LANE_TOO_THIN', 'LANE_TOO_THIN'), ('LANE_CROSSING_DANGEROUS', 'LANE_CROSSING_DANGEROUS'), ('LANE_PRIORITY_NOT_RESPECTED_DANGEROUS', 'LANE_PRIORITY_NOT_RESPECTED_DANGEROUS'), ('LANE_CROSSWALK_MISSING', 'LANE_CROSSWALK_MISSING'), ('RACK_DAMAGED', 'RACK_DAMAGED'), ('NO_BICYCLE_PATH_DANGEROUS_SITUATION', 'NO_BICYCLE_PATH_DANGEROUS_SITUATION'), ('SIGNAGE__MISSING', 'SIGNAGE__MISSING'), ('SIGNAGE__BAD_CONDITION', 'SIGNAGE__BAD_CONDITION'), ('INCIDENT_GLASS_ON_LANE', 'INCIDENT_GLASS_ON_LANE'), ('INCIDENT_NAILS_ON_LANE', 'INCIDENT_NAILS_ON_LANE'), ('ILLEGAL_PARKING', 'ILLEGAL_PARKING'), ('WAL_DANGEROUS_CROSSING', 'WAL_DANGEROUS_CROSSING'), ('WAL_CROWDED_PLACE', 'WAL_CROWDED_PLACE'), ('WAL_DEGRADED_ROAD', 'WAL_DEGRADED_ROAD'), ('WAL_PUDDLE_WATER', 'WAL_PUDDLE_WATER'), ('WAL_LACK_PUBLIC_LIGHTING', 'WAL_LACK_PUBLIC_LIGHTING'), ('WAL_SIGNIFICANT_DROP_ELEVATION', 'WAL_SIGNIFICANT_DROP_ELEVATION'), ('WAL_HIGH_SPEED', 'WAL_HIGH_SPEED'), ('OTHER_IN_COMMENT', 'OTHER_IN_COMMENT')], max_length=540),
        ),
        migrations.AlterField(
            model_name='report',
            name='operation',
            field=models.IntegerField(choices=[(0, 'NONE_OPERATION'), (1, 'LOCALE'), (2, 'BLACK_DOT_WALLONIA')], default=1),
        ),
    ]
