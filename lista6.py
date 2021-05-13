# op = 1
# while op == True:
#     print("---MENU---")
#     print("1 - X-salada")
#     print("2 - Fritas")
#     print("3 - Refrigerante")
#     print("4 - Milkshake")
#     print("5 - Sair do Menu")
#     op = int(input("Digite a opção de acordo com o número: "))
#     if op == 1:
#         print("Você escolheu X-salada")
#         break
#     elif op == 2:
#         print("Você escolheu Fritas")
#         break
#     elif op == 3:
#         print("Você escolheu Refrigerante")
#         break
#     elif op == 4:
#         print("Você escolheu Milkshake")
#         break
#     elif op == 5:
#         print("Você saiu do menu")
#         break
#     else:
#         print("\n\nOpção Inválida!\n\n")
#         op = True

# num = int(input("Digite um número: "))
# soma = 0
# for i in range(1, num):
#     if num%i == 0:
#         soma+=i
# if soma > num:
#     print("Ele é excessivo!")
# elif soma < num:
#     print("Ele não é excessivo!")
# else:
#     print("A soma dos divisores é igual ao número!")

# nome = str(input("Digite o nome do atleta: "))
# print("\n\nDigite o valor dos 5 saltos\n\n")
# salto = float(input("Digite o valor do salto:"))
# maior = salto
# menor = salto
# soma = salto
# n = 5
# if salto == 0:
#     print("Você está fora!")
# else:
#     for i in range(n-1):
#         salto = float(input("Digite o valor do salto:"))
#         if salto > maior:
#             maior = salto
#         elif salto < menor:
#             menor = salto
#         soma+=salto
#     print("A média dos três saltos restantes de ",nome," é de ", (soma-maior-menor)/3)

# n = int(input("Digite o número de motoristas: "))
# soma,tot,maior,d = 0,0,0,0
# for i in range(n):
#     c = int(input("\nInforme o número da carteira de motorista: "))
#     if c >= 1 and c <= 4327:
#         multas = int(input("Digite o número de multas: "))
#         if multas > maior:
#             maior = multas
#             d = c
#         for i in range(multas):
#             val = float(input("Digite o valor de cada multa: "))
#             if val <= 0:
#                 print("Valor inválido!")
#                 break
#             soma+=val
#             tot+=val
#         print("O valor da sua multa é de ",soma)
#         soma = 0
#     else:
#         print("Carteira inválida!")
#         break
# print("\nValor arrecadado com multas: ",tot)
# print("Carteira de motorista com maior numero de multas: ",d)

# print("Digite o número de acordo com o estado")
# print("1 - ACRE")
# print("2 - AMAZONAS")
# print("3 - AMAPÁ")
# print("4 - PARÁ")
# print("5 - RONDÔNIA")
# print("6 - RORAIMA")
# print("7 - TOCANTINS")
# c = int(input("\n\nInforme o código da cidade: "))
# e = int(input("Digite o estado a que pertence: "))
# ca = int(input("Digite o número de carros de passeio: "))
# ac = int(input("Digite o número de acidentes com vítimas: "))
# n,maior,menor,pma,pme,m,me,tot,a,p = 2,ac,ac,c,c,0,0,0,0,0
# if e == 2:
#     m+=ca
#     a+=1
# if e == 4:
#     me+=ac
#     p+=1
# if c <= 0 or e <= 0 or e > 7 or ca <= 0 or ac <= 0:
#     print("Inválido!")
# else:
#     for i in range(n-1):
#         c = int(input("\n\nInforme o código da cidade: "))
#         e = int(input("Digite o estado a que pertence: "))
#         ca = int(input("Digite o número de carros de passeio na cidade: "))
#         ac = int(input("Digite o número de acidentes com vítimas na cidade: "))
#         if c <= 0 or (e <= 0 and e > 7) or ca <= 0 or ac <= 0:
#             print("Inválido!")
#             break
#         else:
#             if ac > maior:
#                 maior = ac
#                 pma = c
#             elif ac < menor:
#                 menor = ac
#                 pme = c
#             if e == 2:
#                 m+=ca
#                 a+=1
#             if e == 4:
#                 me+=ac
#                 p+=1
#             tot+=ca
#     print("\nO maior índice de acidentes é de ",maior," e pertence a cidade ",pma)
#     print("O menor índice de acidentes é de ",menor," e pertence a cidade ",pme)
#     print("A média de veículos é de {:.2f}".format(tot/7)," carros por cidade!")
#     if a != 0 and p != 0:
#         print("A média de veículos no estado de Am é de ", m/a," carros por cidade!")
#         print("A média de acidentes no estado de PA é de ",me/p," por cidade!")

# print("Tabela de código do local")
# print("1 - Residencial")
# print("2 - Comercial")
# print("3 - Industrial")
# n = 1
# op1,op2,op3 = 0,0,0
# s1,s2,s3 = 0,0,0
# while n != 0:
#     n = int(input("\n\nInforme o código do cosumidor: "))
#     if n == 0:
#         break
#     else:
#         qtd = float(input("Digite a quantidade de KWh consumidos: "))
#         op = int(input("Digite a opção de local: "))
#         if op == 1:
#             print("Custo total é de: ",qtd*0.3)
#             op1+=1
#             s1+=(qtd*0.3)
#         elif op == 2:
#             print("Custo total é de: ",qtd*0.5)
#             op2+=1
#             s2+=(qtd*0.5)
#         elif op == 3:
#             print("Custo total é de: ",qtd*0.7)
#             op3+=1
#             s3+=(qtd*0.7)
#         else:
#             print("Opção inválida!")
#             break
# if qtd != 0:
#     print("\nO total de consumo residencial é de ",s1)
#     print("O total de consumo comercial é de ",s2)
#     print("O total de consumo industrial é de ",s3)
#     print("A média de consumo residencial é de {:.2f}".format(s1/op1))
#     print("A média de consumo comercial é de {:.2f}".format(s2/op2))

# s1,s2 = 0,0
# d,t = 0,0
# while d != -1 and t != -1:
#     d = float(input("Digite a sua distância percorrida (em m): "))
#     t = float(input("Digite o tempo gasto (em segundos): "))
#     s1+=d
#     s2+=t
#     if d == 0 and t == 0:
#         s1=s1/1000
#         s2=s2/3600
#         print("A sua velocidade média é de {:.6f}".format(s1/s2)," Km/h")
#         s1,s2 = 0,0
#     elif d == -1 and t == -1:
#         print("Fim!")
        
    