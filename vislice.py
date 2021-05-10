import bottle
import model_vislice

vislice = model_vislice.Vislice()
SKRIVNOST='DanesJeLepDan'

@bottle.get('/')
def osnovna_stran():
    return bottle.template('index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('idigre', id_igre, secret=SKRIVNOST, path ='/')
    bottle.redirect("/igra/")

@bottle.get('/igra/')
def pokazi_igro():
    id_igre = bottle.request.get_cookie('idigre', secret=SKRIVNOST)
    (igra, stanje) = vislice.igre[id_igre]

    return bottle.template("igra.tpl",
                            id_igre = id_igre,
                            igra = igra,
                            poskus = stanje)

@bottle.post('/igra/')
def ugibaj():
    id_igre = bottle.request.get_cookie('idigre', secret=SKRIVNOST)
    crka = bottle.request.forms.getunicode("crka")
    vislice.ugibaj(id_igre, crka)
    bottle.redirect("/igra/")

@bottle.get('/img/<picture>')
def serve_static(picture):
    return bottle.static_file(picture, root="img")

bottle.run(reloader=True, debug=True)




