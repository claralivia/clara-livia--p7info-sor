import tkinter
from tkinter import *
import socket
import pickle


class App(Tk):
    def __init__(self, init):
        Tk.__init__(self, init)
        self.init = init
        self.initialize()

    def calc(self):
        host = socket.gethostname()
        port = 49000

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        self.lblAnswer.destroy()

        data = {}
        data['operator'] = "1"
        data['weight'] = self.txtWeight.get()
        data['height'] = self.txtHeigth.get()

        s.send(pickle.dumps(data))
        print("Enviado...")

        answer = pickle.loads(s.recv(1024))

        s.close()
        texto = "O resultado do seu IMC é {:.2f},\nvocê está {}".format(answer['imc'], answer['msg'])
        self.lblAnswer = Label(self.container5,
                               text=texto,
                               font=self.fonte1,
                               bg='white')
        self.lblAnswer.pack()

    def back(self):
        self.destroy()

    def clear(self):
        self.txtWeight.delete(0, END)
        self.txtHeigth.delete(0, END)
        self.lblAnswer.destroy()

    def initialize(self):
        self.fonte = "Helvetica 12 bold"
        self.fonte1 = "Helvetica 12"

        self.container0 = Frame(None, padx=0, pady=0, bg='white')
        self.container0.pack()
        self.container00 = Frame(None, padx=20, pady=20, bg='white')
        self.container00.pack()
        self.container1 = Frame(None, padx=20, pady=10, bg='white')
        self.container1.pack()
        self.container2 = Frame(None, padx=20, pady=5, bg='white')
        self.container2.pack()
        self.container3 = Frame(None, padx=20, pady=5, bg='white')
        self.container3.pack()
        self.container4 = Frame(None, padx=20, pady=10, bg='white')
        self.container4.pack()
        self.container5 = Frame(None, padx=20, pady=30, bg='white')
        self.container5.pack()
        self.container6 = Frame(None, padx=0, pady=0, bg='white')
        self.container6.pack()

        self.color1 = Label(self.container0,
                            bg='#FF4500',
                            width=20)
        self.color1.pack(side=LEFT)
        self.color2 = Label(self.container0,
                            bg='#FFD700',
                            width=20)
        self.color2.pack(side=LEFT)
        self.color3 = Label(self.container0,
                            bg='#2E8B57',
                            width=20)
        self.color3.pack(side=LEFT)

        self.color4 = Label(self.container6,
                            bg='#FF4500',
                            width=20)
        self.color4.pack(side=LEFT)
        self.color5 = Label(self.container6,
                            bg='#FFD700',
                            width=20,
                            text="Por Clara Lívia",
                            font="Helvetica 9",
                            fg="white")
        self.color5.pack(side=LEFT)
        self.color6 = Label(self.container6,
                            bg='#2E8B57',
                            width=20)
        self.color6.pack(side=LEFT)

        self.titlee = Label(self.container1, text="Informe os dados:",
                           font="Helvetica 16 bold",
                           bg='white')
        self.titlee.pack()

        self.lblWeight = Label(self.container2, text="Massa (kg):",
                               font=self.fonte, width=10,
                               bg='white')
        self.lblWeight.pack(side=LEFT)

        self.txtWeight = Entry(self.container2,
                               width=25,
                               font=self.fonte1,
                               bg='#F5F5F5')
        self.txtWeight.pack(side=LEFT)

        self.lblHeigth = Label(self.container3, text="Altura (m):",
                               font=self.fonte, width=10,
                               bg='white')
        self.lblHeigth.pack(side=LEFT)

        self.txtHeigth = Entry(self.container3,
                               width=25,
                               font=self.fonte1,
                               bg='#F5F5F5')
        self.txtHeigth.pack(side=LEFT)

        self.bntBack = Button(self.container4, text="Sair",
                              font=self.fonte, width=12,
                              command=self.back, bg="#FF4500",
                              fg="white")
        self.bntBack.pack(side=LEFT)

        self.bntCalculate = Button(self.container4, text="Calcular",
                                   font=self.fonte, width=12,
                                   command=self.calc, bg="#FFD700",
                                   fg="white")
        self.bntCalculate.pack(side=LEFT)

        self.bntClear = Button(self.container4, text="Limpar",
                               font=self.fonte, width=12,
                               command=self.clear, bg="#2E8B57",
                               fg="white")
        self.bntClear.pack(side=LEFT)

        self.lblAnswer = Label(self.container00,
                               text="", bg='white')
        self.lblAnswer.pack()

        self.lblAnswer = Label(self.container5,
                               text="", bg='white')
        self.lblAnswer.pack()


if __name__ == "__main__":
    app = App(None)
    app.title('IMC')
    app.configure(bg='white')
    app.mainloop()
