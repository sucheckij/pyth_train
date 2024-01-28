import httpx
import requests
from demos import lista_walut
from bs4 import BeautifulSoup as bs



def demo_web_api_nbp(nbp_flag=True):
    if nbp_flag:
        url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
        req = requests.get(url)
        response = req.json() #parser
        global lista_walut #globalizacja zmiennej

        lista_walut = response[0]['rates']
        print(lista_walut)
        cenaPLN = input("podaj cene PLN: ")
        from lib.utils.validator import isNumber

        if isNumber(cenaPLN):
            cenaPLN = float(cenaPLN)
            print('wybierz walute(number): ')
            for i, w in enumerate(lista_walut):
                print(rf"{i+1} -> {w.get('code')} - {w.get('currency')}")
            waluta = input("Numer waluty: ")
            if waluta.isdigit():
                waluta= int(waluta)-1
                print(f"Cena {lista_walut[waluta]['code']} wynosi {cenaPLN/lista_walut[waluta]['mid']:.2f}")
            else:
                print("Numer musi byc liczba z lewej")

        else:
            print("cena musi byc liczba")


    url_rest_region = "https://restcountries.com/v3.1/all"
    response = requests.get(url_rest_region)
    information = response.json()

    list_of_countries = []
    list_of_regions = []

    for i in information:

        list_of_countries.append(i['name']['common'])

        if i['region'] not in list_of_countries:
            list_of_regions.append(i['region'])

        ## list_of_regions.append(i['region']) # mozna zrobic seta

    list_of_regions = set(list_of_regions)

    print("LIST OF COUNTRIES: ")
    print(list_of_countries)
    print("")
    print("LIST OF REGIONS: ")
    print(list_of_regions)

    response_2 = httpx.get(url_rest_region)
    print("cos")
    pass


def demo_www_scrapping_coronavirus():
    url = 'https://www.worldometers.info/coronavirus/'
    req= requests.get(url)
    zupa = bs(req.text,'html.parser')
    dane_corona = zupa.find_all('div', class_="maincounter-number")
    # print(dane_corona)
    all = dane_corona[0].text.strip().replace(",", " ")
    death = dane_corona[1].text.strip().replace(",", " ")
    recov = dane_corona[2].text.strip().replace(",", " ")
    print(f"Wszystkie przypadki: {all}")
    print(f"Wszystkie przypadki: {death}")
    print(f"Wszystkie przypadki: {recov}")

def www_search_titles():
    search = input("Podaj co chcesz wyszukac: ")
    search.replace(" ", '+')
    url = f'https://helion.pl/search/?qa=&sort=1&szukaj={search}'
    print(url)
    req = requests.get(url)
    zupa = bs(req.text, 'html.parser')
    dane_corona = zupa.find_all('a', class_="short-title", limit=5)
    print(dane_corona)

    list_of_titles = []

    for i in dane_corona:
        string_title = ""
        for n in reversed(list(i)):
            if n == ">" and n>3:
                break
            else:
                string_title+=n
        list_of_titles.append(string_title)
    for i,title in enumerate(list_of_titles):
        print(f"tytul pozycji {i+1} to {title}")

    zmienna = list(enumerate(list_of_titles))
    print(zmienna)