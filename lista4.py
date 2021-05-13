# v = float(input("Digite a sua velocidade (em Km/h): "))
# if v <= 0:
#     print("Velocidade inválida!")
# else:
#     m = v/3.6
#     print("Sua velocidade é de ", m, " m/s")

# s = float(input("Digite seu salário bruto: "))
# if s <= 0:
#     print("Salário inválido!")
# else:
#     ns = s - (s*0.1)
#     sl = ns - (ns*0.05)
#     print("Seu salário líquido é de R$", sl)

# c1 = str(input("Digite o nome do corretor 1: "))
# v1 = float(input("Digite o valor das vendas referentes a ele: "))
# c2 = str(input("Digite o nome do corretor 2: "))
# v2 = float(input("Digite o valor das vendas referentes a ele: "))
# c3 = str(input("Digite o nome do corretor 3: "))
# v3 = float(input("Digite o valor das vendas referentes a ele: "))
# if v1 < 0 or v2 < 0 or v3 < 0:
#     print("Valores de venda inválidos!")
# else:
#     print("\nRELATÓRIO DE VENDAS DOS CORRETORES:")
#     if v1 > 50000:
#         co1 = v1*0.12
#     elif v1 >= 30000 and v1 <= 50000:
#         co1 = v1*0.095
#     else:
#         co1 = v1*0.07

#     if v2 > 50000:
#         co2 = v2*0.12
#     elif v2 >= 30000 and v2 <= 50000:
#         co2 = v2*0.095
#     else:
#         co2 = v2*0.07

#     if v3 > 50000:
#         co3 = v3*0.12
#     elif v3 >= 30000 and v3 <= 50000:
#         co3 = v3*0.095
#     else:
#         co3 = v3*0.07
#     print("Corretor 1:",c1,", com total de venda:",v1," e comissão de:",co1)
#     print("Corretor 2:",c2,", com total de venda:",v2," e comissão de:",co2)
#     print("Corretor 3:",c3,", com total de venda:",v3," e comissão de:",co3)
#     print("\nTotal de vendas da empresa é de: ",v1+v2+v3)

# idade = int(input("Digite sua idade: "))
# if idade <= 0:
#     print("Idade inválida!")
# else:
#     dias = idade*360
#     print("Você já viveu aproximadamente ",dias, "dias")


# valor = int(input("Digite o valor da compra: "))
# p = int(input("Digite o valor que irá pagar: "))
# troco = p - valor
# if valor <= 0 or p <= 0 or troco < 0:
#     print("Valor inválido!")
# elif troco == 0:
#     print("Sem troco")
# else:
#     print("Valor da compra: ",valor,", valor do troco: ",troco)
#     if troco >= 100:
#         t100 = troco - troco%100
#         t100 = t100/100
#         troco = troco - t100*100
#         print(t100," nota(s) de 100")
#     if troco >= 10:
#         t10 = troco - troco%10
#         t10 = t10/10
#         troco = troco - t10*10
#         print(t10," nota(s) de 10")
#     if troco >= 1:
#         t1 = troco
#         print(t1," nota(s) de 1")
    
# print("Definir o número maior, intermediário e menor:")
# a = float(input("Digite um número: "))
# b = float(input("Digite outro número: "))
# c = float(input("Digite outro número: "))
# if a==b or a==c or b==c:
#     print("Alguns ou todos os números são iguais!")
# else:
#     if a > b and a > c:
#         maior = a
#     elif b > a and b > c:
#         maior = b
#     else:
#         maior = c
#     if (a < b and a > c) or (a < c and a > b):
#         intermediario = a
#     elif (b < a and b > c) or (b < c and b > a):
#         intermediario = b
#     else:
#         intermediario = c
#     if a < b and a < c:
#         menor = a
#     elif b < a and b < c:
#         menor = b
#     else:
#         menor = c
#     print("Maior: ",maior," - Intermediário: ",intermediario," - Menor: ",menor)


# a = float(input("Digite um número: "))
# b = float(input("Digite um número: "))
# c = float(input("Digite um número: "))
# d = float(input("Digite um número: "))
# e = float(input("Digite um número: "))
# if a == b or a == c or a == d or a == e or b == c or b == d or b == e or c == d or c == e or d == e:
#     print("Alguns ou todos os números são iguais!")
# else:
#     if a > b and a > c and a > d and a > e:
#         maior = a
#     elif b > a and b > c and b > d and b > e:
#         maior = b
#     elif c > a and c > b and c > d and c > e:
#         maior = c
#     elif d > a and d > b and d > c and d > e:
#         maior = d
#     else:
#         maior = e
     
#     if a < b and a < c and a < d and a < e:
#         menor = a
#     elif b < a and b < c and b < d and b < e:
#         menor = b
#     elif c < a and c < b and c < d and c < e:
#         menor = c
#     elif d < a and d < b and d < c and d < e:
#         manor = d
#     else:
#         menor = e
# print("Maior número: ",maior," e menor número: ",menor)


# nm = str(input("Digite o nome do município: "))
# qtd = int(input("Digite a quantidade de eleitores aptos a votar: "))
# n = int(input("Digite o número de votos do canditado mais votado: "))
# if qtd <= 0 or n <= 0:
#     print("Valores inválidos!")
# else:
#     if qtd < 20000:
#         print("Não terá segundo turno no município de ", nm)
#     else:
#         if n > qtd/2:
#             print("Não terá segundo turno no município de ", nm) 
#         else:
#             print("Terá segundo turno no município de ", nm)


# temp = float(input("Digite a sua temperatura (em Celsius): "))
# if temp >= 39:
#     print("Febre Alta!")
# elif temp >= 37:
#     print("Febril!")
# else:
#     print("Sem Febre!")


# km = float(input("Informe sua distância percorrida (em Km): "))
# h = float(input("Digite o tempo gasto em viagem (em horas): "))
# if km <= 0 or h <= 0:
#     print("Valores inválidos!")
# else:
#     v = km/h
#     if v > 110:
#         print("Sua velocidade média excedeu o limite de velocidade de 110 Km/h!")
#     else:
#         print("Sua velocidade está no limite ou abaixo dele!")


# p1 = float(input("Digite o valor do primeiro produto: "))
# p2 = float(input("Digite o valor do segundo produto: "))
# p3 = float(input("Digite o valor do terceiro produto: "))
# if p1 < p2 and p1 < p3:
#     menor = p1
# elif p2 < p1 and p2 < p3:
#     menor = p2
# else:
#     menor = p3
# print("O produto com menor preço é o de valor igual a ", menor," reais")


# t = str(input("Em qual turno você estuda? (digite V para vespertino, M para matutino ou N para noturno): "))
# if t == 'V' or t == 'v':
#     print("Bom Dia!")
# elif t == 'M' or t == 'm':
#     print("Boa Tarde!")
# elif t == 'N' or t == 'n':
#     print("Boa Noite!")
# else:
#     print("Valor inválido!")


# a = float(input("Digite um número: "))
# b = float(input("Digite um número: "))
# c = float(input("Digite um número: "))
# if a > b and a > c:
#     maior = a
# elif b > a and b > c:
#     maior = b
# else:
#     maior = c
# if a < b and a < c:
#     menor = a
# elif b < a and b < c:
#     menor = b
# else:
#     menor = c
# print("O manor número é ",maior," e o menor é ",menor)


# n = int(input("Digite seu número do cartão (somente o número): "))
# saldo = float(input("Informe seu saldo: "))
# print("Qual operação deseja usar?")
# tipo = str(input("Digite D para depósito ou R para retirada: "))
# if tipo == 'D' or tipo == 'd':
#     print("Quanto deseja depositar?")
#     dep = float(input("Depósito de: "))
#     sf = saldo + dep
#     print("Seu saldo é de ", sf)
# elif tipo == 'R' or tipo == 'r':
#     print("Quanto deseja retirar?")
#     ret = float(input("Retirada de: "))
#     sf = saldo - ret
#     if sf < 0:
#         print("Seu saldo está negativo (",sf,"), conta estourada!")
#     else:
#         print("Seu novo saldo é de ",sf)
# else:
#     print("Operação Inválida!")


# qtd = int(input("Digite a quantidade de dias que ficará no hotel: "))
# if qtd <= 0:
#     print("Quantidade inválida!")
#     valor = 0
# elif qtd > 15:
#     valor = 60 + 5.5*qtd
# elif qtd == 15:
#     valor = 60 + 6*qtd
# else:
#     valor = 60 + 8*qtd
# print("Sua conta por ficar ",qtd," dias no hotel é de ",valor," reais")


# dia = int(input("Digite o dia do seu nascimento: "))
# mes = int(input("Digite o mês do seu nascimento: "))
# if dia <= 0 or mes <= 0 or dia > 31 or mes > 12:
#     print("Dia ou mês inválidos!")
#     singo = "Nada"
# else:
#     if (dia >= 21 and mes == 1) or ( dia <= 19 and mes == 2):
#         signo = "Aquário"
#     elif (dia >= 20 and mes == 2) or ( dia <= 20 and mes == 3):
#         signo = "Peixes"
#     elif (dia >= 21 and mes == 3) or ( dia <= 20 and mes == 4):
#         signo = "Áries"
#     elif (dia >= 21 and mes == 4) or ( dia <= 20 and mes == 5):
#         signo = "Touro"
#     elif (dia >= 21 and mes == 5) or ( dia <= 20 and mes == 6):
#         signo = "Gêmeos"
#     elif (dia >= 21 and mes == 6) or ( dia <= 21 and mes == 7):
#         signo = "Câncer"
#     elif (dia >= 22 and mes == 7) or ( dia <= 22 and mes == 8):
#         signo = "Leão"
#     elif (dia >= 23 and mes == 8) or ( dia <= 22 and mes == 9):
#         signo = "Virgem"
#     elif (dia >= 23 and mes == 9) or ( dia <= 22 and mes == 10):
#         signo = "Libra"
#     elif (dia >= 23 and mes == 10) or ( dia <= 21 and mes == 11):
#         signo = "Escorpião"
#     elif (dia >= 22 and mes == 11) or ( dia <= 21 and mes == 12):
#         signo = "Sagitário"
#     else:
#         signo = "Capricórnio"
# print("Seu signo é ",signo) 


# n = float(input("Digite um número: "))
# print("Escolha a opção de cálculo: ")
# print("MENU")
# print("101 - Raiz Quadrada\n102 - A Metade\n103 - 10% do número\n104 - O Dobro")
# op = int(input("Escolha a opção: "))
# if op == 101:
#     if n < 0:
#         print("Resultado da raiz desse número não existe nos números Reais!")
#     else:
#         print("Raiz quadrada de ",n," é ",(n**(1/2)))
# elif op == 102:
#     print("A metade de ",n," é ",n/2)
# elif op == 103:
#     print("10% de ",n," é ", n*0.1)
# elif op == 104:
#     print("O dobro de ",n," é ",n*2)
# else:
#     print("Opção Inválida!")

# qtd = int(input("Digite a quantidade de maçãs: "))
# if qtd <= 0:
#     print("Valor inválido!")
# else:
#     if qtd >= 12:
#         print("Total da compra: ",qtd," reais")
#     else:
#         print("Total da compra: ",qtd*1.30," reais")
    

# qtd = float(input("Digite a quantidade de litros: "))
# op = str(input("Digite a opção de combustível (A para Álcool ou G para Gasolina): "))
# if qtd <= 0:
#     print("Quantidade inválida!")
# else:
#     if op == 'A' or op == 'a':
#         if qtd > 20:
#             desc = qtd*(2.9 - 2.9*0.05)
#         else:
#             desc = qtd*(2.9 - 2.9*0.03)
#     elif op == 'G' or op == 'g':
#         if qtd > 20:
#             desc = qtd*(3.3 - 3.3*0.06)
#         else:
#             desc = qtd*(3.3 - 3.3*0.04)
#     else:
#         print("Opção Inválida!")
# print("Valor a ser pago será de {:.2f}".format(desc)," reais")


# dM = float(input("Digite a quantidade (em Kg) de morangos: "))
# dMa = float(input("Digite a quantidade (em Kg) de maçãs: "))
# q = dM + dMa
# if dM < 0 or dMa < 0:
#     print("Valor inválido!")
# else:
#     if q <= 5 and q > 0:
#         valor = dM*2.5 + dMa*1.8
#         print("Você deverá pagar o valor de {:.2f}".format(valor)," reais")
#     elif q > 5:
#         valor = dM*2.2 + dMa*1.5
#         if q > 8 or valor > 25:
#             valorD = valor - valor*0.1
#             print("Você deverá pagar o valor de {:.2f}".format(valorD)," reais")
#         else:
#             print("Você deverá pagar o valor de {:.2f}".format(valor)," reais")
#     else:
#         print("Valor Inválido!")

    
# cod = float(input("Digite o código do empregado: "))
# ano = int(input("Digite o ano de nascimento: "))
# emp = int(input("Digite o ano que ele entrou na empresa: "))
# idade = 2019 - ano
# t = 2019 - emp
# if ano <= 0 or emp <= 0 or idade <= 0 or t < 0:
#     print("Valor inválido!") 
# elif idade >= 60:
#     if t >= 25:
#         print("Idade: ",idade,", Tempo de Trabalho: ",t,". Requerer Aposentadoria!")
#     elif idade >= 65:
#         print("Idade: ",idade,", Tempo de Trabalho: ",t,". Requerer Aposentadoria!")
#     else:
#         print("Idade: ",idade,", Tempo de Trabalho: ",t,". Não Requerer!")
# elif t >= 30:
#     print("Idade: ",idade,", Tempo de Trabalho: ",t,". Requerer Aposentadoria!")
# else:
#     print("Idade: ",idade,", Tempo de Trabalho: ",t,". Não Requerer!")

# peso = float(input("Digite seu peso (em Kg): "))
# alt = float(input("Digite sua altura (em m): "))
# if peso <= 0 or alt <= 0:
#     print("Valor Inválido!")
# else:
#     imc = peso/(alt**2)
#     if imc > 30:
#         print("Obesidade!")
#     elif imc >= 25:
#         print("Acima do Peso!")
#     elif imc >= 18.5:
#         print("Peso Normal!")
#     else:
#         print("Abaixo do Peso!")

# peso = float(input("Digite a quantidade de peixes (em Kg): "))
# if peso <= 0:
#     print("Valor inválido!")
# else:
#     if peso > 50:
#         k = peso - 50
#         v = k*4
#         print("Você irá pagar ",v," reais de multa!")
#     else:
#         print("Você não pagará nada!")