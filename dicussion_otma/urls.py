
import django
from django.contrib import admin
from django.urls import path, include
from omtaapp import views as omta_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Page d'accueil
    path('', omta_views.pageentre, name='pageentre'),

    # Saisie checklist
    path('checklist/', omta_views.CheckList_view, name='checklist'),
    
    # Login / authentification
    path('accounts/login/', omta_views.user_login, name='login'),
    path('accounts/loginn/', omta_views.user_loginn, name='loginn'),

    # Pages après login
    path('accounts/login/formule', omta_views.htmlfile_view, name='htmlfile'),
    path('accounts/loginn/valide', omta_views.validefile_view, name='validefile'),

    # Inclusion des urls du module accounts (vérifie bien le nom du fichier : urls.py)
    path('accounts/', include('accounts.url')),  # Pluriel recommandé

    # Liste des checklists à valider (page validateur)
  

    # Modifier validation d'une checklist (POST)
    
    path('modifier_checklists/', omta_views.modifier_checklists, name='modifier_checklists'),

    path('checklists/', omta_views.validefile_view, name='liste_checklists'),
  


    path('validefile/', omta_views.modifier_checklists, name='validefile'),
    
    path('logout/', omta_views.logout_view, name='logout'),


    #path('changer_statut/<int:fiche_id>/', omta_views.changer_statut, name='changer_statut'),
]
