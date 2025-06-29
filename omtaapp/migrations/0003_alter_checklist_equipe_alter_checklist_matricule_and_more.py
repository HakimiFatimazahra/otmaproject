# Generated by Django 5.2 on 2025-06-16 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omtaapp', '0002_alter_checklist_fil2_l2_theorique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='equipe',
            field=models.CharField(choices=[('Equipe01', 'Equipe01'), ('Equipe02', 'Equipe02'), ('Equipe03', 'Equipe03'), ('Equipe04', 'Equipe04')], max_length=50),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='matricule',
            field=models.CharField(choices=[('Komax01', 'Komax01'), ('Komax02', 'Komax02'), ('Komax03', 'Komax03'), ('Komax04', 'Komax04'), ('Komax05', 'Komax05')], max_length=50),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='motif',
            field=models.CharField(choices=[('Démarrage série', 'Démarrage série'), ('Changement de référence', 'Changement de référence'), ('Intervention maintenance', 'Intervention maintenance')], max_length=50),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='validation_status',
            field=models.CharField(choices=[('En attente', 'En attente'), ('Valide', 'Valide'), ('Non-Valide', 'Non-Valide')], default='En attente', max_length=20),
        ),
    ]
