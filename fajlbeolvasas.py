from Film import Film
film_lista = []

def beolvas():
    f = open("film.txt", "r", encoding="utf-8")
    f.readline()
    fajl_tartalom = f.readlines()
    f.close()
    feldolgoz(fajl_tartalom)

def feldolgoz(fajl_tartalom):
    i = 0
    while i < len(fajl_tartalom):
        sorlista = fajl_tartalom[i].strip().split(";")
        film = Film(sorlista)
        film_lista.append(film)
        i += 1

    print(film_lista[2].cim)


#add meg az adatok sorainak a számát (az első sor nélkül)!
def filmek_szama():
    return len(film_lista)


#Melyik a legrövidebb film címe?
def legrovidebb():
    min = film_lista[0].perc
    minhely = 0
    i = 0
    while i < len(film_lista):
        if film_lista[i].perc < min:
            min = film_lista[i].perc
            minhely = i
        i += 1

    return film_lista[minhely].cim


#Hány darab legalább 110 perces film van?
def szaztizperc():
    i = 0
    szaztizesek = 0
    while i < len(film_lista):
        if int(film_lista[i].perc) >= 110:
            szaztizesek += 1
        i += 1
    return szaztizesek


#Kérd be egy színész nevét, és ajánlj egy pár filmet a készletből, ha tudsz (film címét íratjuk ki, ha van ilyen)! Ha nincs ilyen nevű színész, akkor azt is tudasd!
def film_ajanlo():
    film_cime = []
    szinesz_neve = input("Kérem adjon meg egy színészt a kereséshez:")
    i = 0
    while i < len(film_lista):
        if (film_lista[i].foszereplo == szinesz_neve):
            film_cime.append(film_lista[i].cim)
        i += 1
    if len(film_cime) <= 0:
        return "Nincs ilyen színésszel film"
    else:
        return film_cime


#A 4-es feladat eredményét írasd ki fájlba is!
def fajl_beiras(eredmeny):
    f = open("film2.txt", "w", encoding="utf-8")
    #f.write(str(szaztizperc()))
    f.write(str(eredmeny))
    f.close()

