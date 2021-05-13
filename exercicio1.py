# nomeA = str(input("Digite seu nome: "))
# a = int(input("Digite a sua quantidade de pontos: "))
# nomeB = str(input("Digite seu nome: "))
# b = int(input("Digite a sua quantidade de pontos: "))
# nomeC = str(input("Digite seu nome: "))
# c = int(input("Digite a sua quantidade de pontos: "))
# if a == b and b == c:
#     print("Todos os jogaores tiveram a mesma pontuação!")
# elif a==b and b>c:
#     print("Os jogadores ", nomeA, " e ", nomeB," tiveram a mesma pontuação: (",a,") e em segundo colocado: ",nomeC," - ",c," pontos")
# elif a==b and b<c:
#     print("Vencedor: ",nomeC," - ",c," pontos e os jogadores ", nomeA, " e ", nomeB," tiveram a mesma pontuação: (",a,") e ficaram em segundo lugar")
# elif a>b:
#     if b>c:
#         print("Vencedor: ", nomeA," - ", a, "pontos \nSegundo colocado: ", nomeB," - ",b," pontos \nTerceiro colocado: ", nomeC, " - ",c, "pontos")
#     elif c>b and c<a:
#         print("Vencedor: ", nomeA," - ", a, "pontos \nSegundo colocado: ", nomeC," - ",c," pontos \nTerceiro colocado: ", nomeB, " - ",b, "pontos")
#     else:
#         print("Vencedor: ", nomeC," - ", c, "pontos \nSegundo colocado: ", nomeA," - ",a," pontos \nTerceiro colocado: ", nomeB, " - ",b, "pontos")
# elif b>a:
#     if a>c:
#         print("Vencedor: ", nomeb," - ", b, "pontos \nSegundo colocado: ", nomeA," - ",a," pontos \nTerceiro colocado: ", nomeC, " - ",c, "pontos")
#     elif c>a and c<b:
#         print("Vencedor: ", nomeB," - ", b, "pontos \nSegundo colocado: ", nomeC," - ",c," pontos \nTerceiro colocado: ", nomeA, " - ",a, "pontos")
#     else:
#         print("Vencedor: ", nomeC," - ", c, "pontos \nSegundo colocado: ", nomeB," - ",b," pontos \nTerceiro colocado: ", nomeA, " - ",a, "pontos")
# else:
#     print("Outra combinação ou alguns dos números são iguais")

# idade = int(input("Digite sua idade: "))
# if idade < 18:
    # if idade >= 16:
        # print("Eleitor Facultativo!")
    # else:
        # if idade <= 0:
            # print("Idade inválida!")
        # else:
            # print("Não Eleitor!")
# elif idade >= 18:
    # if idade <= 65:
        # print("Eleitor Obrigatório!")
    # else:
        # print("Eleitor Facultativo!")

#num1 = float(input("Digite um número: "))
#num2 = float(input("Digite outro número: "))
#sinal = str(input("DIGITE:\n+ para somar \n- para subtrair \n* para multiplicar \n/ para dividir: "))
#if sinal == '+':
#    print("A soma de ", num1, " e ", num2," é de ", num1+num2)
#elif sinal == '-':
#    print("A subtração de ", num1, " e ", num2," é de ", num1-num2)
#elif sinal == '*':
#    print("A multiplicação de ", num1, " e ", num2," é de ", num1*num2)
#elif sinal == '/':
#    if num1 == 0 or num2 == 0:
#        print("Por favor não digite 0 em uma divisão!")
#    else:
#        print("A divisão de ", num1, " e ", num2," é de ", num1/num2)
#else:
#    print("Sinal inválido!")

#nota1 = float(input("Digite sua 1º nota: "))
#nota2 = float(input("Digite sua 2º nota: "))
#nota3 = float(input("Digite sua 3º nota: "))
#mp = (nota1*2 + nota2*4 + nota3*4)/10
#if mp >= 8:
#    print("Você está aprovado com ", mp)
#else:
#    if mp >= 5:
#        print("Tem direito à prova final, e sua nota foi ", mp)
#    else:
#        print("Reprovado com nota ", mp)

#num = int(input("Digite um número: "))
#if num%2 == 0:
#    print("Ele é par")
#else:
#    print("Ímpar")

#salarioBruto = float(input("Digite seu salário bruto: "))
#emp = float(input("Digite o valor do empréstimo: "))
#qtd = int(input("Digite a quantidade de parcelas: "))
#if (emp/qtd) <= (salarioBruto*0.3):
#    print("Empréstimo concedido!")
#else:
#    print("Empréstimo não concedido!")