# coding: latin-1

#!/usr/bin/python
import cgitb, cgi
cgitb.enable()

form = cgi.FieldStorage()

button = int(form.getvalue('button'))

#TEMPERATURA:
if button == 1:
    valorUm = float(form.getvalue('valorUm'))
    deTemp = form.getvalue('deTemp')
    paraTemp = form.getvalue('paraTemp')
    if deTemp == '1':
        if paraTemp == '1':
            valor = valorUm
            tipo = '°C'
        elif paraTemp == '2':
            valor = (valorUm * (9/5)) + 32
            tipo = '°F'
        elif paraTemp == '3':
            valor = valorUm + 273.15
            tipo = 'K'
    elif deTemp == '2':
        if paraTemp == '1':
            valor = (valorUm - 32)*(5/9)
            tipo = '°C'
        elif paraTemp == '2':
            valor = valorUm
            tipo = '°F'
        elif paraTemp == '3':
            valor = (valorUm - 32)*(5/9)+273.15
            tipo = 'K'
    elif deTemp == '3':
        if paraTemp == '1':
            valor = valorUm-273.15
            tipo = '°C'
        elif paraTemp == '2':
            valor = (valorUm-273.15)*(9/5)+32
            tipo = '°F'
        elif paraTemp == '3':
            valor = valorUm
            tipo = 'K'


#COMPRIMENTO:
if button == 2:
    valorDois= float(form.getvalue('valorDois'))
    deComp = form.getvalue('deComp')
    paraComp = form.getvalue('paraComp')
    if deComp == '1':
        if paraComp == '1':
            valor = valorDois
            tipo = 'cm'
        elif paraComp == '2':
            valor = valorDois/100
            tipo = 'm'
        elif paraComp == '3':
            valor = valorDois/100000
            tipo = 'km'
    elif deComp == '2':
        if paraComp == '1':
            valor = valorDois*100
            tipo = 'cm'
        elif paraComp == '2':
            valor = valorDois
            tipo = 'm'
        elif paraComp == '3':
            valor = valorDois/1000
            tipo = 'km'
    elif deComp == '3':
        if paraComp == '1':
            valor = valorDois*100000
            tipo = 'cm'
        elif paraComp == '2':
            valor = valorDois*1000
            tipo = 'm'
        elif paraComp == '3':
            valor = valorDois
            tipo = 'km'


#MASSA:
if button == 3:
    valorTres = float(form.getvalue('valorTres'))
    deMassa = form.getvalue('deMassa')
    paraMassa = form.getvalue('paraMassa')
    if deMassa == '1':
        if paraMassa == '1':
            valor = valorTres
            tipo = 'mg'
        elif paraMassa == '2':
            valor = valorTres/1000
            tipo = 'g'
        elif paraMassa == '3':
            valor = valorTres/1000000
            tipo = 'kg'
    elif deMassa == '2':
        if paraMassa == '1':
            valor = valorTres*1000
            tipo = 'mg'
        elif paraMassa == '2':
            valor = valorTres
            tipo = 'g'
        elif  paraMassa == '3':
            valor = valorTres/1000
            tipo = 'kg'
    elif deMassa == '3':
        if paraMassa == '1':
            valor = valorTres/1000000
            tipo = 'kg'
        elif paraMassa == '2':
            valor = valorTres*1000
            tipo = 'g'
        elif paraMassa == '3':
            valor = valorTres
            tipo = 'Kg'

valor = str(valor).replace('.', ',')


print("Content-Type:text/html\r\n\r\n")
print("""
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Conversor de Medidas</title>
</head>
<style>
body{
    font-family: "Montserrat", "Helvetica";
    margin: 0px;
}

.header{
    background-color: #707070;
    font-size: 30pt;
    font-weight: bolder;
    color: #FFF;
    border-radius: 0px 0px 30px 30px;
    height: 130px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.footer{
    background-color: #707070;
    font-size: 10pt;
    color: #FFF;
    border-radius: 30px 30px 0px 0px ;
    height: 75px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
a{
    color: #FFF;
    text-decoration:none;
}
form{
    display: flex;
    justify-content: center;
    align-items: center;
}
.center{   
    display: block;
    justify-content: center;
    align-items: center;
}
.resultado{
    font-size: 70pt;
    font-weight: bolder;
    color: #707070;
    display: block;
    text-align: center;
    padding-top: 135px;
    padding-bottom: 135px;
}

</style>""")
print('<body>')
print('<div class="header">Conversor de Medidas</div')
print('<div class="center">')
print('<form>')
print('<div class="resultado">O resultado é:<br/> %s %s</div>' % (valor, tipo))
print('</form>')
print('</div>')
print('<div class="footer"><a href="https://github.com/claralivia">Desenvolvido por Clara Lívia</a></div>')
print('</body>')
print('</html>')
        