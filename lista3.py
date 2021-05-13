#valor = float(input("Digite o valor total das despesas: "))
#gorjeta = valor*0.1
#print("O valor da gorjeta é de: ", gorjeta)

#custoF = float(input("Digite o valor do custo de fábrica do carro: "))
#distribuidor = custoF*0.12
#impostos = custoF*0.45
#print("O custo ao consumidor será de ", custoF+distribuidor+impostos)

#nome = str(input("Digite o nome do vendedor: "))
#qtd = int(input("Digite a quantidade de carros vendidos por este vendedor: "))
#vt = float(input("Digite o valor total de vendas realizadas por este vendedor: "))
#salario = 500 + 50*qtd + vt*0.05
#print("Senhor(a) ", nome, ", seu salário é de R$", salario)

#print("----CARDÁPIO----")
#print("\nHamburguer---------- R$ 3,00")
#print("X-Burguer----------- R$ 2,50")
#print("Fritas-------------- R$ 2,50")
#print("Refrigerante-------- R$ 1,00")
#print("Milkshake----------- R$ 3,00")
#h = int(input("Digite a quantidade de Hambúrguer's que deseja: "))
#x = int(input("Digite a quantidade de X-Burguer's que deseja: "))
#f = int(input("Digite a quantidade de Fritas que deseja: "))
#r = int(input("Digite a quantidade de Refrigerantes que deseja: "))
#m = int(input("Digite a quantidade de Milkshake's que deseja: "))
#ct = h*3 + x*2.5 + f*2.5 + r*1 + m*3
#if h < 0 or x < 0 or f < 0 or r < 0 or m < 0: 
#    print("Algum dos valores digitados é menor que 0!")
#else:
#    print("A conta final deu R$", ct)

#num = int(input("Digite um número: "))
#if num%5 == 0:
#    print("É divisível por 5!")
#else:
#    print("Não é divisível por 5!")

#num = int(input("Digite um número: "))
#if num%3 == 0 and num%7 == 0:
#    print("É divisível por 3 e por 7!")
#else:
#    print("Não divisível por 3 e por 7!")

#num = int(input("Digite um número: "))
#if (num%4 == 0 and num%8 == 0) or (num%6 == 0 and num%9 == 0):
#    print("Ele é múltiplo ou de 4 e 8 ou de 6 e 9")
#else:
#    print("Ele não é múltiplo nem de 4 e 8 nem de 6 e 9")

#nome = str(input("Digite seu nome: "))
#sexo = str(input("Digite M para masculino ou F para feminino: "))
#idade = int(input("Digite sua idade: "))
#if (sexo == 'F' or sexo == 'f') and (idade < 25):
#    print("Parabéns, ", nome, ", você foi aceita!")
#elif (sexo == 'M' or sexo == 'm') or (idade > 25 or idade <= 0):
#    print("Você, ", nome, ", não foi aceita(o)")
#else:
#    print("Sexo ou idade inválida!")


#l1 = float(input("Digite um lado do triângulo: "))
#l2 = float(input("Digite um outro lado do triângulo: "))
#l3 = float(input("Digite um outro lado do triângulo: "))
#if l1 <= 0 or l2 <= 0 or l3 <= 0:
#    print("Nenhum lado de triângulo pode ser menor ou igual a 0!")
#elif l1 == l2 and l2 == l3:
#    print("Triângulo Equilátero!")
#elif (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l2 != l1):
#    print("Triângulo Isósceles!")
#elif l1 != l2 and l2 != l3 and l3 != l1:
#    print("Triângulo Escaleno!")
#else:
#    print("As medidas não compõem um triângulo!")

#idade = int(input("Digite sua idade: "))
#if idade >= 0 and idade < 5:
#    print("Nenhuma categoria!")
#elif idade >= 5 and idade <= 7:
#    print("Categoria: Infantil A")
#elif idade >= 8 and idade <= 10:
#    print("Categoria: Infantil B")
#elif idade >= 11 and idade <= 13:
#    print("Categoria: Juvenil A")
#elif idade >= 14 and idade <= 17:
#    print("Categoria: Juvenil B")
#elif idade >= 18 and idade <= 122:
#    print("Categoria: Sênior")
#else:
#    print("Idade Inválida!")

#num = int(input("Digite um número: "))
#if num == 5:
#    print("Seu número é igual a 5!")
#elif num == 200:
#    print("Seu número é igual a 200!")
#elif num == 400:
#    print("Seu número é igual a 400!")
#elif num >= 500 and num <= 1000:
#    print("Seu número está entre 500 e 100!")
#else:
#    print("Seu número não está em nenhuma das opções anteriores!")

#sal = float(input("Digite seu salário: "))
#if sal > 0 and sal <= 600:
#    print("Você está isento, seu salário é de R$", sal)
#elif sal > 600 and sal <= 1200:
#    print("Seu salário sofrerá desconto de 20%, seu salário é de R$ ", (sal - (sal*0.2)))
#elif sal > 1200 and sal <= 2000:
#    print("Seu salário sofrerá desconto de 25%, seu salário é de R$ ", (sal - (sal*0.25)))
#elif sal > 2000:
#    print("Seu salário sofrerá desconto de 30%, seu salário é de R$ ", (sal - (sal*0.3)))
#else:
#    print("Salário Inválido!")

#valor = float(input("Digite o valor do produto: "))
#if valor > 0 and valor < 20:
#    print("O valor da venda do produto será de R$", valor + (valor*0.45))
#elif valor >= 20:
#    print("O valor da vendo do produto será de R$", valor + (valor*0.3))
#else:
#    print("Valor inválido!")

#mes = int(input("Digite um número de 1 a 12: "))
#if mes == 1:
#    print("Janeiro!")
#elif mes == 2:
#    print("Fevereiro!")
#elif mes == 3:
#    print("Março!")
#elif mes == 4:
#    print("Abril!")
#elif mes == 5:
#    print("Maio!")
#elif mes == 6:
#    print("Junho!")
#elif mes == 7:
#    print("Julho!")
#elif mes == 8:
#    print("Agosto!")
#elif mes == 9:
#    print("Setembro!")
#elif mes == 10:
#    print("Outubro!")
#elif mes == 11:
#    print("Novembro!")
#elif mes == 12:
#    print("Dezembro!")
#else:
#    print("Mês inválido!")

#sexo = str(input("Digite M para masculino e F para feminino: "))
#alt = float(input("Digite sua altura (em metros): "))
#if alt < 0.2:
#    print("Altura inválida!")
#else: 
#    if sexo == 'M' or sexo == 'm':
#        print("Seu peso ideal é de ", (72.7*alt) - 58, " Kg")
#    elif sexo == 'F' or sexo == 'f':
#        print("Seu peso ideal é de ", (62.1*alt) - 44.7, " Kg")
#    else:
#        print("Sexo inválido!")
    
