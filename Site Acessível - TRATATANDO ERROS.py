#CRIE UM CÓDIGO EM PYTHON QUE TESTE SE O SITE PUDIM ESTÁ ACESSÍVEL PELO COMPUTADOR USADO

import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site Pudim')
    print(site.read()) # consegue pegar o conteúdo html do site