from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.

def characters(request):
    titulo_pagina = "CHARACTERS"
    if request.method == 'POST':
        texto_base = request.POST['text']
        if 'Capitalize' in request.POST:
            resposta = texto_base.capitalize()
        elif 'Upper' in request.POST:
            resposta = texto_base.upper()
        elif 'Lower' in request.POST:
            resposta = texto_base.casefold()
        elif 'Swapcase' in request.POST:
            resposta = texto_base.swapcase()
        elif 'Title' in request.POST:
            resposta = texto_base.title()
        else:
            resposta = texto_base
        dados = {
            'resposta': resposta,
            'titulo' : titulo_pagina
        }
        return TemplateResponse(request, 'words/characters.html', dados)
    else:
        titulo_pagina = "CHARACTERS"
        dados = {
            'titulo' : titulo_pagina
        }
        print(dados)
        dados = {"nome":"edson"}
        return render(request, 'words/characters.html', dados)

def enconding(request):
    titulo_pagina = "ENCONDING"
    if request.method == 'POST':
        pass
    else:
        dados = {
            'titulo' : titulo_pagina
        }
        print(dados)
        dados = {"nome":"edson"}
        return render(request, 'words/enconding.html', dados)

def chartoNumbers(request):
    titulo_pagina = "CHAR TO NUMBER"
    if request.method == 'POST':
        pass
    else:
        dados = {
            'titulo' : titulo_pagina
        }
        print(dados)
        dados = {"nome":"edson"}
        return render(request, 'words/chartoNumbers.html', dados)