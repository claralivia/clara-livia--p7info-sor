## Conversor de Medidas - CGI com Python

Desenvolver uma aplicação que rode em um servidor HTTP usando scripts Python com CGI. A aplicação deve apresentar um formulário para o usuário realizar consultas e receber a resposta do servidor para implementar um conversor de unidades de medidas. A aplicação deve oferecer ao usuário pelo menos duas opções de grandezas (por exemplo, tempo e comprimento) e para cada grandeza pelo menos 3 conversões (Por exemplo, Tempo: minutos para segundos, horas para segundos e horas para minutos).

### Permitindo a execução do script
No seu terminal dê o seguinte comando:
```sh
chmod -x result.py
```
_(substitua `result.py` por seu script)_

### Iniciando o servidor
Rodar usando o comando seguinte no terminal, para iniciar o servidor de testes do python: 
```sh
python -m http.server 8080 --cgi
```
_(você pode usar outras portas, ao invés da `8080` e outros servidores web, como o [Apache](https://httpd.apache.org/docs/2.2/howto/cgi.html) por exemplo)_

### Acessando o formulário
Abra a seguinte página no navegador:

[http://localhost:8080/form.html](http://localhost:8080/form.html)

_(substitua a porta `8080` pela que você está usando e `form.html` pela sua página inicial)_
