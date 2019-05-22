% import model
<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>

  <h2>{{igra.pravilni_del_gesla()} }</h2>

  Nepravilne črke : {{igra.nepravilni_ugibi()}}

  % preostali_poskusi = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1, igra.nepravilni_ugibi()
  Število preostalih poskusov: {{preostali_poskusi}}

</body>

</html>