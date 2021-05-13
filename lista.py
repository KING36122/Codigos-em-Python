# print(l)
# l.append(4)
# print(l)
# l.append(10000)
# print(l)
# l.insert(1,100)
# print(l)
# l.remove(10000)
# print(l)
# l.pop(5)
# print(l)
# l[0] = 0
# print(l)
# # l[8] = 99 #não pode usar um índice que não está no range
# # print(l)
# l = [1,2,3,4,5,6,7, "Meliodinhas", "Diane", "Ban", "King", "Gowther", "Merlin", "Escanor"]
# print(l)
# l = ["Meliodas", "Diane", "Ban", "King", "Gowther", "Merlin", "Escanor"]
# t = len(l)
# for i in range(t):
#     print(l[i])
# import random
# lista = []
# n = random.randrange(20, 101)
# for i in range(n):
#     num = random.randrange(1,1001)
#     lista.append(num)
# print(lista)
# print(n)
# print(len(lista))
# print(max(lista))
# print(min(lista))
# t = len(lista)
# maior = lista[0]
# menor = lista[0]
# for i in range(1,t):
#     if lista[i] > maior:
#         maior = lista[i]
#     elif lista[i] < menor:
#         menor = lista[i]
# print(maior)
# print(menor)
# print(max(lista)+min(lista))
# print(sum(lista))

import random
lista = []
n = 10
for i in range(n):
    num = random.randrange(1,1001)
    lista.append(num)
lista.sort()
print(lista)
# lista.sort()
# print(lista)
# lista.reverse()
# print(lista)

x = int(input("Número: "))
a = 0

for i in range(n):
    if lista[i] == x:
        a = [i]
print(a)