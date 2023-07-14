# Generated by Django 4.2.2 on 2023-07-14 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0003_rename_body_part_training_part_num_bodypart_part_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='part_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training', to='workout.bodypart'),
        ),
    ]
