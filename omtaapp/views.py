from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from .models import CheckList

# Vue pour gérer la saisie d'un checklist (POST + création objet)
def CheckList_view(request):
    if request.method == 'POST':
        matricule = request.POST.get('matricule')
        machine = request.POST.get('machine')
        date = request.POST.get('date')
        sf = request.POST.get('sf')
        mp = request.POST.get('mp')
        equipe = request.POST.get('equipe')
        motif = request.POST.get('motif')
        controle_bobines = request.POST.get('controle_bobines')
        pression_entree = request.POST.get('pression_entree') or None
        pression_courroie = request.POST.get('pression_courroie') or None
        aspect = request.POST.get('aspect')
        verification_blo = request.POST.get('verification_blo')
        validation_status = request.POST.get('validation_status', 'En attente')

        fil1_nom = request.POST.get('fil1_nom')
        fil1_L1_theorique = request.POST.get('fil1_L1_theorique')
        fil1_L1_mesuree = request.POST.get('fil1_L1_mesuree')

        fil2_nom = request.POST.get('fil2_nom')
        fil2_L2_theorique = request.POST.get('fil2_L2_theorique')
        fil2_L2_mesuree = request.POST.get('fil2_L2_mesuree')

        cmp1_num = request.POST.get('cmp1_num')
        miniapp1 = request.POST.get('miniapp1')
        cmp1_hc_min = request.POST.get('cmp1_hc_min')
        cmp1_hc_max = request.POST.get('cmp1_hc_max')
        cmp1_hc_mesuree = request.POST.get('cmp1_hc_mesuree')
        cmp1_hr_min = request.POST.get('cmp1_hr_min')
        cmp1_hr_max = request.POST.get('cmp1_hr_max')
        cmp1_hr_mesuree = request.POST.get('cmp1_hr_mesuree')
        cmp1_tr_min = request.POST.get('cmp1_tr_min')
        cmp1_tr_mesuree = request.POST.get('cmp1_tr_mesuree')

        cmp2_num = request.POST.get('cmp2_num')
        miniapp2 = request.POST.get('miniapp2')
        cmp2_hc_min = request.POST.get('cmp2_hc_min')
        cmp2_hc_max = request.POST.get('cmp2_hc_max')
        cmp2_hc_mesuree = request.POST.get('cmp2_hc_mesuree')
        cmp2_hr_min = request.POST.get('cmp2_hr_min')
        cmp2_hr_max = request.POST.get('cmp2_hr_max')
        cmp2_hr_mesuree = request.POST.get('cmp2_hr_mesuree')
        cmp2_tr_min = request.POST.get('cmp2_tr_min')
        cmp2_tr_mesuree = request.POST.get('cmp2_tr_mesuree')

        CheckList.objects.create(
            matricule=matricule,
            machine=machine,
            date=date,
            sf=sf,
            mp=mp,
            equipe=equipe,
            motif=motif,
            controle_bobines=controle_bobines,
            pression_entree=pression_entree,
            pression_courroie=pression_courroie,
            aspect=aspect,
            verification_blo=verification_blo,
            validation_status=validation_status,

            fil1_nom=fil1_nom,
            fil1_L1_theorique=fil1_L1_theorique,
            fil1_L1_mesuree=fil1_L1_mesuree,

            fil2_nom=fil2_nom,
            fil2_L2_theorique=fil2_L2_theorique,
            fil2_L2_mesuree=fil2_L2_mesuree,

            cmp1_num=cmp1_num,
            miniapp1=miniapp1,
            cmp1_hc_min=cmp1_hc_min,
            cmp1_hc_max=cmp1_hc_max,
            cmp1_hc_mesuree=cmp1_hc_mesuree,
            cmp1_hr_min=cmp1_hr_min,
            cmp1_hr_max=cmp1_hr_max,
            cmp1_hr_mesuree=cmp1_hr_mesuree,
            cmp1_tr_min=cmp1_tr_min,
            cmp1_tr_mesuree=cmp1_tr_mesuree,

            cmp2_num=cmp2_num,
            miniapp2=miniapp2,
            cmp2_hc_min=cmp2_hc_min,
            cmp2_hc_max=cmp2_hc_max,
            cmp2_hc_mesuree=cmp2_hc_mesuree,
            cmp2_hr_min=cmp2_hr_min,
            cmp2_hr_max=cmp2_hr_max,
            cmp2_hr_mesuree=cmp2_hr_mesuree,
            cmp2_tr_min=cmp2_tr_min,
            cmp2_tr_mesuree=cmp2_tr_mesuree,
        )
        return redirect('checklist')
    return render(request, 'htmlfile.html')


# Fonctions pour vérifier les groupes
def is_saisisseur(user):
    return user.groups.filter(name='Saisisseur').exists()

def is_validateur(user):
    return user.groups.filter(name='Validateur').exists()


# Vues protégées
@login_required
@user_passes_test(is_saisisseur)
def saisie_view(request):
    return render(request, 'saisie.html')

@login_required
@user_passes_test(is_validateur)
def validation_view(request):
    return render(request, 'valider.html')


# Pages simples
def signup(request):
    return render(request, 'signup.html')

def pageentre(request):
    return render(request, 'pageentre.html')

def htmlfile_view(request):
    return render(request, 'htmlfile.html')

def login_page(request):
    return render(request, 'login.html')

def loginn_page(request):
    return render(request, 'loginn.html')

def validefile_view(request):
    return render(request, 'validefile.html')


# Connexion utilisateur - saisisseur
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('htmlfile')
        else:
            return render(request, 'login.html', {'error': 'Login ou mot de passe incorrect.Essayez encore'})
    else:    
        return render(request, 'login.html')


# Connexion utilisateur - validateur
def user_loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('validefile')
        else:
            return render(request, 'loginn.html', {'error': 'Login ou mot de passe incorrect.Essayez encore'})
    return render(request, 'loginn.html')
from django.contrib.auth import logout
from django.shortcuts import redirect
def logout_view(request):
    logout(request)
    return redirect('pageentre') 

from django.contrib.auth.decorators import login_required

@login_required(login_url='pageentre')
def dashboard(request):
    return render(request, 'dashboard.html')



# Changement du statut de validation
@login_required
@user_passes_test(is_validateur)
@require_POST
def modifier_validation(request, checklist_id):
    checklist = get_object_or_404(CheckList, id=checklist_id)
    validation_status = request.POST.get('validation_status')

    if validation_status in ['En attente', 'Valide', 'Non-Valide']:
        checklist.validation_status = validation_status
        checklist.save()

    return redirect('liste_checklists')



from django.db.models import Case, When, Value, IntegerField



@login_required
@user_passes_test(is_validateur)
def validefile_view(request):
    filtre_statut = request.GET.get('filtre_statut', '')
    print("Filtre demandé :", filtre_statut)

    if filtre_statut:
        checklists = CheckList.objects.filter(validation_status=filtre_statut)
    else:
        checklists = CheckList.objects.all()

    return render(request, 'validefile.html', {
        'checklists': checklists,
        'filtre_statut': filtre_statut
    })



from django.shortcuts import render, redirect
from omtaapp.models import CheckList

def modifier_checklists(request):
    if request.method == "POST":
        print("POST reçu !")
        print("Données POST reçues :", request.POST)

        for checklist_id, new_status in request.POST.items():
            if checklist_id.startswith("status_"):
                pk = checklist_id.replace("status_", "")
                try:
                    checklist = CheckList.objects.get(pk=pk)
                    checklist.validation_status = new_status
                    checklist.save()
                    print(f"Mise à jour de l'objet {pk} avec le statut : {new_status}")
                except CheckList.DoesNotExist:
                    print(f"Checklist avec id {pk} introuvable.")

        return redirect('validefile')

    checklists = CheckList.objects.all
    
    return render(request, 'validefile.html', {'checklists': checklists})
from django.shortcuts import render
from .models import CheckList
from django.db.models import Count
import json

def dashboard_view(request):
    total_fiches = CheckList.objects.count()
    par_statut = list(CheckList.objects.values('validation_status').annotate(total=Count('id')))
    par_machine = list(CheckList.objects.values('machine').annotate(total=Count('id')))

    context = {
        'total_fiches': total_fiches,
        'par_statut': json.dumps(par_statut),
        'par_machine': json.dumps(par_machine),
    }
    return render(request, 'dashboard.html', context)
