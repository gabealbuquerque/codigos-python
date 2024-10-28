import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
