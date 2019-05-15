import model
lojtrice = "#####################\n"
def zacetek_igre(igra):
    tekst = lojtrice + "Evo kolega, ze pa v nizki štart, začni ugibat, pa nea se zmoti, ker maš že štrik okol vrata. Maš  {0}, zaj pa začni!\n".format(igra.pravilni_del_gesla())
    return tekst
    
def izpis_zmage(igra):
    tekst = lojtrice + "Pa ka si ti ja nor! Vgano si, da sn mislo {0}. Ala ti vera, stari!.\n".format(igra.geslo)
    return tekst

def izpis_poraza(igra):
    tekst = lojtrice + "HAHA! Obeso sn te! Vbistvu je blo prav {0}.\n".format(igra.geslo)
    return tekst

def izpis_igre(igra):
    tekst = (lojtrice + igra.pravilni_del_gesla() + "\n" + 
            ("Življenja: {0}" + "\n" + 
            "Napake: {1}").format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1, igra.nepravilni_ugibi()) + lojtrice)
    return tekst

def zahtevaj_vnos():
    return input("Ugibaj te že, kolega:  ")

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        # izpišemo stanje igre
        print(izpis_igre(igra))
        # zahtevamo vnos uporabnika
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)
        # preveri, ali smo končasi
        if igra.poraz():
            print(izpis_poraza(igra))
            break
        if igra.zmaga():
            print(izpis_zmage(igra))
            break
        else:
            pass
    return None

pozeni_vmesnik()




# igra = model.nova_igra()
# igra.ugibaj("a")
# print(izpis_zmage(igra))
# print(izpis_poraza(igra))
# print(izpis_igre(igra))