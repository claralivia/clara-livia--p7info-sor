import time
from datetime import datetime
import threading

def fun(id, data, status):
    mensagem =  " | hello, world"
    dados = "ID: " + str(id) + mensagem + " | Data: " + str(data) + " | Status: " + str(status)
    print(dados)
    time.sleep(2)
    status = "Finalizada"
    data = datetime.today().strftime("%Hh%Mm%Sseg")
    dados = "ID: " + str(id) + mensagem + " | Data: " + str(data) + " | Status: " + str(status)
    print(dados)

x = int(input("Qual o número de threads? "))

id = 0
for i in range(x):
    id = id + 1
    y = threading.Thread(target=fun, args=(id, datetime.today().strftime("%Hh%Mm%Sseg"), "Iniciada"))
    y.start()

