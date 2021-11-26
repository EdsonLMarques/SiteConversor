from django.shortcuts import render
from django.template.response import TemplateResponse
from django.contrib import messages

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
    resposta = ""
    if request.method == 'POST':
        texto_base = request.POST['text']
        if 'C0NV3RT' in request.POST:
            resposta = convert(texto_base)
        elif 'binary' in request.POST:
            resposta = binary(texto_base)
        elif 'octal' in request.POST:
            pass
        elif 'hex' in request.POST:
            pass
        elif 'latters_to_morse' in request.POST:
            if('.' in texto_base or '-' in texto_base):
                resposta = texto_base
            else:
                resposta = encrypt(texto_base.upper())
        elif 'morse_to_letters' in request.POST:
            if('.' in texto_base or '-' in texto_base):
                resposta = decrypt(texto_base)
            else:
                resposta = texto_base
        else:
            pass
        dados = {
            'resposta':resposta,
            'titulo' : titulo_pagina
        }
        return TemplateResponse(request, 'words/enconding.html', dados)
    else:
        dados = {
            'titulo' : titulo_pagina
        }
        print(dados)
        dados = {"nome":"edson"}
        return render(request, 'words/enconding.html', dados)

#functions

def convert(texto):
    texto_final = texto.replace('a','4')
    texto_final = texto_final.replace('e','3')
    texto_final = texto_final.replace('i','1')
    texto_final = texto_final.replace('o','0')
    texto_final = texto_final.replace('u','u')
    texto_final = texto_final.replace('A','4')
    texto_final = texto_final.replace('E','3')
    texto_final = texto_final.replace('I','1')
    texto_final = texto_final.replace('O','0')
    texto_final = texto_final.replace('U','U')
    return texto_final


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher.strip()

def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher.strip()

def binary(texto):
    a_string = texto
    a_byte_array = bytearray(a_string, "utf8")
    byte_list = []
    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(binary_representation)
    resposta = " ".join(byte_list)
    return resposta
