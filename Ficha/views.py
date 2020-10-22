from django.shortcuts import render, redirect

from Ficha.form import FichaForm
from Ficha.models import Ficha


# Create your views here.


def ficha_list(request):
    player = Ficha.objects.filter(tipo='player')
    npc = Ficha.objects.filter(tipo='npc')
    return render(request, 'Ficha/ficha_lista.html', {'Fichas_jogador': player, 'Fichas_npc': npc})


def ficha_detail(request, id):
    data = {}
    ficha = Ficha.objects.get(id=id)
    form = FichaForm(request.POST or None, instance=ficha)
    data['Ficha'] = ficha
    data['form'] = form
    if form.is_valid():
        form.save()
        return redirect('ficha_lista')
    else:
        return render(request, 'Ficha/ficha_detail.html', data)
