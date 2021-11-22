import socket
import pickle
import time
import threading

def handle_client(conn, addr):
    currentTime = time.ctime((time.time()))
    print("Estabelecendo uma conexão com %s às %s." % (str(addr), currentTime))
    data = pickle.loads(conn.recv(1024))

    if data['operator'] == "1":
        w = float(data['weight'])
        h = float(data['height'])

        imcs = {}
        imcs['imc'] = w / (h * h)
        print("IMC calculado com sucesso!")

        if imcs['imc'] < 18.5:
            imcs['msg'] = "abaixo do peso. \nIsso é preocupante!"
        elif imcs['imc'] < 25:
            imcs['msg'] = "no peso normal. \nContinue assim!"
        elif imcs['imc'] < 30:
            imcs['msg'] = "com sobrepeso. \nAlerta!"
        elif imcs['imc'] < 35:
            imcs['msg'] = "com obesidade de grau 1. \nCuide da sua alimentação!"
        elif imcs['imc'] < 40:
            imcs['msg'] = "com obesidade de grau 2. \nVocê tem que se cuidar urgentemente."
        else:
            imcs['msg'] = "com obesidade de grau 3. \nVocê está correndo perigo!!!"

        time.sleep(10)
        conn.send(pickle.dumps(imcs))

        conn.close()


host = socket.gethostname()
port = 49000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

print("\nEcho server iniciado!", end="")
print("\tAguardando uma conexão...")

while True:
      conn, addr = s.accept()
      t = threading.Thread(target=handle_client, args=(conn,addr))
      t.start()