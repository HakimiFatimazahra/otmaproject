from django.db import models

class CheckList(models.Model):
    # Choix
    Komax = [('Komax01','Komax01'), ('Komax02','Komax02'), ('Komax03','Komax03'), ('Komax04','Komax04'), ('Komax05','Komax05')]
    equipe_choices = [('Equipe01','Equipe01'),('Equipe02','Equipe02'),('Equipe03','Equipe03'),('Equipe04','Equipe04')]
    motif_choices = [('Démarrage série','Démarrage série'),('Changement de référence','Changement de référence'),('Intervention maintenance','Intervention maintenance')]
    OK_NOK_CHOICES = [('OK', 'OK'), ('NOK', 'NOK')]

    # Champs principaux
    machine = models.CharField(max_length=50, choices=Komax)
    matricule_Saisie = models.CharField(max_length=50)
    matricule_Valider = models.CharField(max_length=50)
    date = models.DateField()
    sf = models.CharField(max_length=50)
    mp = models.CharField(max_length=50)
    equipe = models.CharField(max_length=50, choices=equipe_choices)
    motif = models.CharField(max_length=50, choices=motif_choices)

    # Contrôles simples
    controle_bobines = models.CharField(max_length=50, choices=OK_NOK_CHOICES)
    pression_entree = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pression_courroie = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    aspect_bobines = models.CharField(max_length=50, choices=OK_NOK_CHOICES)
    aspect = models.CharField(max_length=50, choices=OK_NOK_CHOICES)
    verification_blo = models.CharField(max_length=50, choices=OK_NOK_CHOICES)

    # Longueur Fil 1
    fil1_nom = models.CharField(max_length=50)
    fil1_L1_theorique = models.DecimalField(max_digits=10, decimal_places=2)
    fil1_L1_mesuree = models.DecimalField(max_digits=10, decimal_places=2)

    # Longueur Fil 2
    fil2_nom = models.CharField(max_length=50)
    fil2_L2_theorique = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fil2_L2_mesuree = models.DecimalField(max_digits=10, decimal_places=2)

    # CMP 1
    cmp1_num = models.CharField(max_length=50)
    miniapp1 = models.CharField(max_length=50)
    cmp1_hc_min = models.DecimalField(max_digits=10, decimal_places=2)
    cmp1_hc_max = models.DecimalField(max_digits=10, decimal_places=2)
    cmp1_hc_mesuree = models.DecimalField(max_digits=10, decimal_places=2)
    cmp1_hr_min = models.DecimalField(max_digits=10, decimal_places=2)
    cmp1_hr_max = models.DecimalField(max_digits=10, decimal_places=2)
    cmp1_hr_mesuree = models.DecimalField(max_digits=10, decimal_places=2)
    cmp1_tr_min = models.DecimalField(max_digits=10, decimal_places=2)
    cmp1_tr_mesuree = models.DecimalField(max_digits=10, decimal_places=2)

    # CMP 2
    cmp2_num = models.CharField(max_length=50)
    miniapp2 = models.CharField(max_length=50)
    cmp2_hc_min = models.DecimalField(max_digits=10, decimal_places=2)
    cmp2_hc_max = models.DecimalField(max_digits=10, decimal_places=2)
    cmp2_hc_mesuree = models.DecimalField(max_digits=10, decimal_places=2)
    cmp2_hr_min = models.DecimalField(max_digits=10, decimal_places=2)
    cmp2_hr_max = models.DecimalField(max_digits=10, decimal_places=2)
    cmp2_hr_mesuree = models.DecimalField(max_digits=10, decimal_places=2)
    cmp2_tr_min = models.DecimalField(max_digits=10, decimal_places=2)
    cmp2_tr_mesuree = models.DecimalField(max_digits=10, decimal_places=2)

    # Statut de validation
    STATUTS_CHOICES = [
        ('En attente', 'En attente'),
        ('Valide', 'Valide'),
        ('Non-Valide', 'Non-Valide'),
    ]
    validation_status = models.CharField(max_length=20, choices=STATUTS_CHOICES, default='En attente')

    def __str__(self):
        return f"CheckList {self.machine} - {self.date}"
