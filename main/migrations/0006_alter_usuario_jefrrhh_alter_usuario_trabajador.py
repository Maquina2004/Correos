# Generated by Django 4.2.7 on 2024-06-09 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_usuario_jefrrhh_alter_usuario_trabajador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='jefRRHH',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='trabajador',
            field=models.BooleanField(default=True),
        ),
    ]
