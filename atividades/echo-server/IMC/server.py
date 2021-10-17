import socket
import pickle

host = socket.gethostname()
port = 50000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen()

print("\nEcho server iniciado!", end="")
print("\tAguardando uma conexão...")

while True:
    conn, addr = s.accept()
    print("%s : %s foi conectado." % addr)

    data = pickle.loads(conn.recv(1024))

    if data['operator'] == "1":
        w = float(data['weight'])
        h = float(data["height"])

        imcs = {}
        h = h/100
        w = w/100
        imcs['imc'] = w/(h*h)
        print("IMC calculado com sucesso!")

        if imcs['imc'] < 18.5:
            imcs['msg'] = "abaixo do peso."
        elif imcs['imc'] < 25:
            imcs['msg'] = "no peso normal."
        elif imcs['imc'] < 30:
            imcs['msg'] = "com sobrepeso."
        elif imcs['imc'] < 35:
            imcs['msg'] = "com obesidade de grau 1."
        elif imcs['imc'] < 40:
            imcs['msg'] = "com obesidade de grau 2."
        else:
            imcs['msg'] = "com obesisdade de grau 3."

        conn.send(pickle.dumps(imcs))

        conn.close()
