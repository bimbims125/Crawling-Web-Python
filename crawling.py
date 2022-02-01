from bs4 import BeautifulSoup
import requests
import pandas as pd

def menu():
    pilih = int(input('1.Crawl Web.\n2.Tampilkan Hasil.\n3.Exit. \nPilih menu:'))
    if pilih == 1:
        crawlWeb()
    elif pilih == 2:
        tampilData()
    else:
        print('Terima Kasih')
        # exit()

def crawlWeb():
    url = input('Masukkan URL: ')
    r = requests.get(url)
    
    request = r.content
    soup = BeautifulSoup(request, 'html.parser')
    
    elemen = input('Masukkan elemen yang akan dicari: ')
    attr = input('Masukkan atribut yang akan dicari: ')
    klas = input('Masukkan klas yang akan dicari: ')
    
    konten = soup.findAll(elemen, attrs={attr:klas})
    
    global data
    data = []
    for k in konten:
        data.append(k.text.strip())
    menu()
    
def tampilData():
    df = pd.DataFrame(data)
    print(df)
    menu()
    
menu()
