import bottle
import model

bottle.TEMPLATE_PATH.insert(0, 'U:\\_Osebno\\Profile.V6\\FAKS\\UVP\\Vislice\\datoteke\\views')

vislice = model.Vislice()
id_testne_igre = vislice.nova_igra()
vislice.ugibaj(id_testne_igre, 'A')

@bottle.get('/')
def index():
    return bottle.template('index.tpl')

@bottle.get('/igra/')
def testna_igra():
    return bottle.template('igra.tpl',
    igra = vislice.igre[id_testne_igre][0],
    id_igre = id_testne_igre,
    poskus = vislice.igre[id_testne_igre][1])


bottle.run(reloader=True, debug=True)