# -*- coding: utf-8 -*-

/*Definindo as linhas*/
line1 = ['Lista de Produtos', 'QTD Entradas', 'QTD Saídas', 'Saldo Estoque', 'Preço Unitário', 'Subtotal']
line2 = ['Azeite de Oliva - Extra Virgem LAT 500ml', 100, 40, 60, 21.90, 1304.00]
line3 = ['Castanha do Pará - Granel (Gr)', 100, 5, 95, 6.00, 300.00]
line4 = ['Flocos de Aveia CXA 500g', 1000, 200, 800, 10.90, 872.00]
line5 = ['Paçoca de Amendoim - CXA 30 Und', 100, 8, 92, 1.50, 30.00]
line6 = ['Panetone sem Gluten - CXA 1 Und', 100, 60, 40, 17.30, 692.00]
line7 = ['Pão Sirio Integral -  Saco 500g', 100, 70, 30, 5.90, 177.00]
line8 = ['Polpa de Açai Natural - PCT 5L', 100, 1, 99, 7.10, 639.00]
line9 = ['Queijo Vegano| - PCT 450g', 100, 30, 70, 25.00, 1750.00]
line10 = [ "","","","", 'Total', 5774.00]

/*Formatando as linhas*/
def lines(line):
    print("+", end="")
    for i in range(0, 162):
      print("-", end="")
    print("+", end="")
    print("\n| {:<50}| {:^20}| {:^20}| {:^20}| {:^20}| {:^20} |".format(*line))
    
/*Imprimindo as linhas*/
lines(line1)
lines(line2)
lines(line3)
lines(line4)
lines(line5)
lines(line6)
lines(line7)
lines(line8)
lines(line9)
lines(line10)

/*Última linha da tabela*/
print("+", end="")
for i in range(0, 162):
   print("-", end="")
print("+", end="")
