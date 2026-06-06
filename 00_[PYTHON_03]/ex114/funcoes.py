import urllib.request
import urllib.error

def lin():
    print('=-='*10)

def pudim():
    try:
        url = 'http://www.pudim.com.br'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(url, headers=headers)
        site = urllib.request.urlopen(req)
    except urllib.error.URLError as erro:
        print('Site Pudim.com.br Não Está Acessivel!')
    else:
        print('Site Pudim.com.br Está Acessivel!')