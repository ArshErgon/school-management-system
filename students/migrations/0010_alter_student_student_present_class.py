# Generated by Django 3.2.9 on 2021-12-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_alter_student_student_present_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_present_class',
            field=models.CharField(choices=[('NUSERY', 'NUSERY'), ('LKG', 'LKG'), ('UKG', 'UKG'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='Nusery', max_length=10),
        ),
    ]
