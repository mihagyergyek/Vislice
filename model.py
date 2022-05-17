import json

STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'
ZMAGA, PORAZ = 'W', 'X'
ZACETEK = 'Z'
DATOTEKA_S_STANJEM = "stanje.json"

class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        if crke is not None:
            self.crke = crke
        else:
            self.crke = []

    def napacne_crke(self):
        return[crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return[crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return len(set(self.geslo)) == len(self.pravilne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka
            else:
                niz += '_'
        return niz

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:    
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            elif crka in self.geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

with open("besede.txt", encoding= 'utf-8') as d:
    bazen_besed = []
    for beseda in d:
        bazen_besed.append(beseda.strip())

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)

class Vislice:
    datoteka_s_stanjem = DATOTEKA_S_STANJEM

    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if not self.igre:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        i = self.prost_id_igre()
        igra = nova_igra()
        self.igre[i] = (igra, ZACETEK)
        return i

    def ugibaj(self, i, crka):
        igra, stanje = self.igre[i]
        stanje = igra.ugibaj(crka)
        self.igre[i] = (igra, stanje)

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, encoding='utf-8') as d:
            zapis = json.load(d)
        for id_igre, ((geslo, crke), stanje) in zapis.items():
            self.igre[id_igre] = (Igra(geslo, crke), stanje)

    def zapisi_igre_v_datoteke(self):
        igre = {}
        for id_igre, (igra, stanje) in self.igre.items():
            igre[id_igre] = ((igra.geslo, igra.crke), stanje)
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as d:
            json.dump(igre, d)

#with open("besede.txt", encoding='utf-8') as d:
#   bazen_besed = d.read().split('\n')        