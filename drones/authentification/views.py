from django.shortcuts import render


def connexion(request):
    if request.method == 'POST':
        # Vérification des informations d'authentification
        # et connexion de l'utilisateur si les informations sont valides
        pass
    else:
        return render(request, 'authentification/connexion.html')
# Create your views here.
