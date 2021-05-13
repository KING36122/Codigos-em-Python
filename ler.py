# n = int(input("Digite: "))
# maior = n
# menor = n
# for i in range(4):
#     n = int(input("Digite: "))
#     if n > maior:
#         maior = n
#     elif n < menor:
#         menor = n
# print("Maior: ",maior,"\nMenor: ",menor)


# alt = float(input("Digite sua altura: "))
# sexo = int(input("Digite 1 para masculino ou 2 para feminino: "))
# menor = alt
# maior = alt
# n = 0
# m = 0
# soma = 0
# h = 0
# if sexo == 2:
#     m += 1
#     soma += alt
# elif sexo == 1:
#     h += 1
# else:
#     print("Sexo errado!")
# if (sexo == 1 or sexo == 2) and alt!=0:
#     while alt != 0 and n < 4:
#         alt = float(input("Digite sua altura: "))
#         sexo = int(input("Digite 1 para masculino ou 2 para feminino: "))
#         if sexo == 2:
#             m += 1
#             soma += alt
#         elif sexo == 1:
#             h += 1
#         else:
#             print("Sexo errado!")
#             break
#         if alt > maior:
#             maior = alt
#         elif alt < menor:
#             menor = alt
#             n += 1
#     print(menor)
#     print(maior)
#     if soma == 0 or m == 0:
#         print("Nada")
#     else:
#         print(soma/m)
#     print(h)
# else:
#     print("Altura errada!")

# a = 1
# menor = a
# maior = a
# n = 0
# m = 0
# soma = 0
# h = 0
# alt = 1
# while alt != 0:
#     alt = float(input("Digite sua altura: "))
#     if alt == 0:
#         print("Altura errada!")
#         sexo = 0
#         break
#     else:
#         sexo = int(input("Digite 1 para masculino ou 2 para feminino: "))
#         if sexo == 2:
#             m += 1
#             soma += alt
#         elif sexo == 1:
#             h += 1
#         else:
#             print("Sexo errado!")
#             break
#         if alt > maior:
#             maior = alt
#         elif alt < menor:
#             menor = alt
#             n += 1
# if (sexo == 1 or sexo == 2):        
#     print(menor)
#     print(maior)
#     if soma == 0 or m == 0:
#         print("Nada")
#     else:
#         print(soma/m)
#     print(h)

# num = 1
# a = 1
# menor = a
# maior = a
# soma = 0
# h = 0
# alt = 1
# while num != 0:
#     num = float(input("Digite seu número: "))
#     if num == 0:
#         print("Número errado!")
#         break
#     else:
#         peso = int(input("Digite o peso do boi: "))
#         if peso > maior:
#             maior = peso
#         elif peso < menor:
#             menor = peso
#     h+=1
# print("Maior: ",maior," - Menor: ",menor," Total de bois: ", h)

num = int(input("Digite um número: "))
for i in range(1, num+1):
    if num%i == 0:
        print(i)


