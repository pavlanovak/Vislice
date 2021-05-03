import model_vislice

PONOVNI_ZAGON = 'p'
IZHOD = 'i'

def izpis_igre(igra):
    tekst = f"""############################\n
    Pravilni del gesla: {igra.pravilni_del_gesla()}\n
    Število poskusov: {model_vislice.STEVILO_DOVOLJENIH_NAPAK + 1 - igra.stevilo_napak()} \n
    Nepravilne črke: {igra.nepravilni_ugibi()}
    #################################### \n
    """
    return tekst

def izpis_zmage(igra):
    tekst = f"""################################\n
    Bravo! Zmagali ste!\n 
    Uganili ste geslo: {igra.pravilni_del_gesla()}\n
    ######################### \n"""
    return tekst

def izpis_poraza(igra):
    tekst = f"""################################\n
    Porabili ste vse poskuse.\n 
    Pravilno geslo: {igra.geslo}\n
    ############################ \n"""
    return tekst

def nesmiseln_izpis(crka):
    tekst = f"""##########################\n
    Vnesite nekaj smiselnega!\n
    Na primer 'a'.\n
    ################################\n"""
    return tekst

def zahtevaj_vnos():
    return input('Vnesite črko: ')

def zahtevaj_moznost():
    return ('Vnesite možnost: ')

def ponudi_moznosti():
    tekst = f""" Vpišite črko za izbor naslednjih možnosti:\n 
    {PONOVNI_ZAGON} : ponovni zagon igre \n 
    {IZHOD} : izhod \n
    """
    return tekst

def izberi_ponovitev():
    input(ponudi_moznosti())
    moznost = zahtevaj_moznost().strip().lower()
    if moznost == PONOVNI_ZAGON:
        igra = model_vislice.nova_igra()
        print(izpis_igre(igra))
        return igra
    else:
        return IZHOD

def pozeni_vmesnik():
    igra = model_vislice.nova_igra()
    while True:
        crka = zahtevaj_vnos()
        if crka.isnumeric() or len(crka) > 1 or not crka.isalnum():
            print(nesmiseln_izpis(crka))
        else:
            odziv = igra.ugibaj(crka)
            if odziv == model_vislice.ZMAGA:
                print(izpis_zmage(igra))
                igra = izberi_ponovitev()
                if igra == IZHOD:
                    break
            elif odziv == model_vislice.PORAZ:
                print(izpis_poraza(igra))
                igra = izberi_ponovitev()
                if igra == IZHOD:
                    break           
            else:
                print(izpis_igre(igra))




pozeni_vmesnik()
