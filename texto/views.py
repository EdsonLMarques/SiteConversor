from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        texto_base = request.POST['text']
        if 'Capitalize' in request.POST:
            resposta = texto_base.capitalize()
        elif 'Upper' in request.POST:
            resposta = texto_base.upper()
        elif 'Lower' in request.POST:
            resposta = texto_base.casefold()
        elif 'Encode' in request.POST:
            resposta = texto_base.encode(encoding='base64')
        elif 'Swapcase' in request.POST:
            resposta = texto_base.swapcase()
        elif 'Title' in request.POST:
            resposta = texto_base.title()
        else:
            resposta = texto_base

        dados = {
            'resposta': resposta
        }
        return TemplateResponse(request, 'index.html', dados)
    else:   
        print('sem metodo ') 
        dados = {"nome":"edson"}
        return render(request, 'index.html', dados)
        