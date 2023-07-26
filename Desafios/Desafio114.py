import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print("Erro na conexão com a internet ou a URL não foi encontrada")
else:
    print("Conexão estabelecida com sucesso!")