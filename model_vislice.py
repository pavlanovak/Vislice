STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'
ZACETEK = 'S'

import random 
import json

class Igra:
    
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke[:]
    
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        vse_crke = True
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                pass
            else:
                vse_crke = False
                break
        #vse_crke1 = all(crka in self.crke for crka in self.geslo)
        return vse_crke and STEVILO_DOVOLJENIH_NAPAK >= self.stevilo_napak()

    def poraz(self):
        return STEVILO_DOVOLJENIH_NAPAK < self.stevilo_napak()
    
    def pravilni_del_gesla(self):
        pravilni_del = ''
        ugibanje = [crka.upper() for crka in self.crke]
        for i in self.geslo:
            if i.upper() in ugibanje:
                pravilni_del += i
            else:
                pravilni_del += ' _'
        return pravilni_del
    
    def nepravilni_ugibi(self):
        locen_niz = ''
        for i in self.crke:
            if i not in self.geslo:
                locen_niz += i + ' '
            else:
                pass
        return locen_niz[:-1]
        #' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
with open('/Users/pavlanovak/Desktop/uvp 2021/vislice/Besede.txt', 'r') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]


    def nova_igra():
        geslo = random.choice(bazen_besed)
        return Igra(geslo, [])
    
    class Vislice:

        def __init__(self, stanje, datoteka_z_besedami):
            self.igre = {}
            self.datoteka_s_stanjem = stanje
            self.datoteka_z_besedami = datoteka_z_besedami
        
        def prost_id_igre(self):
            if self.igre == {}:
                return 0
            else:
                return max(self.igre.keys()) + 1
        
        def nova_igra(self):
            self.nalozi_igre_iz_datoteke()
            with open(self.datoteka_z_besedami, 'r') as f:
                bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]
            igra = nova_igra()
            geslo = random.choice(bazen_besed)
            igra = Igra(geslo, [])
            id_igre = self.prost_id_igre()
            self.igre[id_igre] = (igra, ZACETEK)
            self.zapisi_igro_v_datoteko()
            return id_igre
        
        def ugibaj(self, id_igre, crka):
            self.nalozi_igre_iz_datoteke()
            (igra, _) = self.igre[id_igre]
            stanje = igra.ugibaj(crka)
            self.igre[id_igre] = (igra, stanje)
            self.zapisi_igro_v_datoteko()
        
        def zapisi_igro_v_datoteko(self):
            with open(self.datoteka_s_stanjem, 'w') as f:
                igre_predelano = {id_igre : ((igra.geslo, igra.crke), stanje) for (id_igre, (igra, stanje)) in self.igre.items()}
                json.dump(igre_predelano, f)

        def nalozi_igre_iz_datoteke(self):
            with open(self.datoteka_s_stanjem, 'r') as f:
                igre_predelano = json.load(f)
                self.igre = { int(id_igre): (Igra(geslo, crke), stanje) for (id_igre, ((geslo, crke), stanje)) in igre_predelano.items()}





#testno_geslo = 'DE??UJE'
#testne_crke = ['A', 'E', 'I', 'O', 'U', 'D', 'J', 'K', '??']
#igra = Igra(testno_geslo, testne_crke)


#testno_geslo_2 = 'DE??UJE'
#testne_crke_2 = ['A', 'E', 'I', 'O', 'U', 'D', 'J']
#igra2 = Igra(testno_geslo_2, testne_crke_2)