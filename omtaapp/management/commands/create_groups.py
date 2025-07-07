from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User

class Command(BaseCommand):
    help = 'Crée les groupes Saisisseur et Validateur et crée des utilisateurs de test'

    def handle(self, *args, **kwargs):
        groupes = {
            'SaisisseurOne': {
                'users': [
                    {'username': 'saisisseur1', 'password': 'azerty123'},
                    {'username': 'saisisseur2', 'password': 'azerty23'},
                ]
            },
            'ValidateurOne': {
                'users': [
                    {'username': 'validateur1', 'password': 'azerty'},
                    {'username': 'validateur2', 'password': 'azerty13'},
                ]
            }
        }

        for group_name, group_data in groupes.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Groupe '{group_name}' créé."))
            else:
                self.stdout.write(self.style.WARNING(f"Groupe '{group_name}' déjà existant."))

            for user_data in group_data['users']:
                username = user_data['username']
                password = user_data['password']

                if not User.objects.filter(username=username).exists():
                    user = User.objects.create_user(username=username, password=password)
                    user.groups.add(group)
                    user.save()
                    self.stdout.write(self.style.SUCCESS(f"Utilisateur '{username}' créé et ajouté à '{group_name}'."))
                else:
                    self.stdout.write(self.style.WARNING(f"Utilisateur '{username}' existe déjà."))
