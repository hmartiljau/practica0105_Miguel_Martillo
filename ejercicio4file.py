import urllib.request
def read_url(url):
    file = urllib.request.urlopen(url)
    #file = open('saludo.txt', 'r')
    leer=file.read()
    separador=leer.split()
    print(len(separador))
url = "http://textfiles.com/adventure/aencounter.txt"
read_url(url)



















