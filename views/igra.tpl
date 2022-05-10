<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

Geslo: {{ geslo }}<br/>
Nepravilni ugibi: {{ nepravilni }}<br/>
<img src="/img/{{obesenost}}.jpg" alt="obesanje">
% if stanje != model.ZMAGA and stanje != model.PORAZ:
<form action="" method="post">
    <input name="crka" autofocus> <input type="submit" value="Ugibaj">
</form>
% elif stanje == model.ZMAGA:
Čestitke, zmagali ste! Bi želeli igrati še enkrat?
<form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
</form>
% elif stanje == model.PORAZ:
Več sreče prihodnjič., geslo je bilo <b>{{celo_geslo}}</b>
Bi želeli igrati še enkrat?
<form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
</form>
% end
</body>

</html>