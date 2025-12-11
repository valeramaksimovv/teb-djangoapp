from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(req):
    #print(req)
    return render(req, 'start.html')
  
@csrf_exempt
def logowanie(req):
    #print(req.POST.keys())
    wysylka = { 'login': req.GET['user'] if 'user' in req.GET.keys() else 'Gość', 'informacja': 'Nie jesteś zalogowany, spróbuj zrobić to przez poniższy formularz' }
    if (len(req.POST.keys()) > 0 and req.POST['login'] == 'admin' and 
    req.POST['pass'] == 'TajneHaslo'):
        wysylka = {'login': req.POST['login'], 'informacja': f"Witaj {req.POST['login']}, z hasłem {req.POST['pass']}" }
    
    return render(req, 'login.html', wysylka)



def technologies(req):
    return render(req, 'technologies.html')


def photos(req):
    return render(req, 'photos.html')
