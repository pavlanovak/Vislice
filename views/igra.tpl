% import model_vislice
<!DOCTYPE html>
<html>
<body>
<table>
    <tr>
    <td>
{{igra.pravilni_del_gesla()}}
    </td>
    </tr>
    <tr>
    <td>

        <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">

</td>
</tr>
<tr>
<td>
    Nepravilne črke:
    {{igra.nepravilni_ugibi()}}


</td>
</tr>
</table>
</body>
% if poskus == model_vislice.ZMAGA :

<h1>Zmaga!</h1>
Uganili ste pravilno geslo. Čestitke!

<form action="/igra/" method="get">
    <button type="submit">Nova igra</button>


% elif poskus == model_vislice.PORAZ :
<h2>Izgubili ste!</h2>
Pravilno geslo je: {{igra.geslo}}

<form action="/igra/" method="get">
    <button type="submit">Nova igra</button>
% else :   
 <form action="/igra/{{id_igre}}/" method="post">
    <input type ="text" name="crka" autofocus>
    <button type="submit">Ugibaj!</button>
</form>
% end
</html>