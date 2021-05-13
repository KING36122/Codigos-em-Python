# soma = 0
# for i in range(85, 907):
#     if i%2==0:
#         print(i)
#         soma+=i
# print(soma)

# par = 0
# im = 0
# n = int(input("Informe quantos números você vai digitar: "))
# for i in range(n):
#     num = int(input("Digite: "))
#     if num%2==0 and num!=0:
#         par += 1
#     elif num == 0:
#         par+=0
#         im+=0
#     else:
#         im += 1
# print("Números pares: ",par, " e números ímpares: ",im)

# num = int(input("Digite o número da base: "))
# exp = int(input("Digite o número da potência: "))
# valor = 1
# for i in range(exp):
#     valor = valor * num
# print(valor)

# num = int(input("Digite um valor: "))
# valor = 1
# i = 1
# if num < 0:
#     print("Valor inválido!")
# else:
#     while i <= num:
#         valor = valor * i
#         i+=1
#     print("O valor de ",num,"! é de: ",valor)

# num = int(input("Digite um número: "))
# soma = 0
# for i in range(1, num):
#     if num%i == 0:
#         soma += i
# if soma == num:
#     print("Número perfeito!")
# else:
#     print("Não é um número perfeito!")

# soma = 0
# c = 0
# for i in range(50):
#     num = int(input("Digite um valor: "))
#     if num > 0:
#         soma+=num
#     elif num < 0:
#         c+=1
# print("Soma dos positivos: ",soma," e qtd de negativos: ",c)

# maior = 0
# soma = 0
# i = 0
# while i < 15:
#     cod = int(input("Digite o código do produto: "))
#     val = float(input("Digite o valor do produto: "))
#     if val <= 0:
#         print("Valor inválido!")
#         break
#     else:
#         if val > maior:
#             maior = val
#         soma+=val
#         i+=1
# print("O maior valor é: ",maior," e a média dos preços é de ",soma/i)

# soma = 0
# for i in range(10):
#     num = int(input("Digite um número: "))
#     if num < 40:
#         soma+=num
# print(soma)

# cm = 0
# cf = 0
# for i in range(50):
#     nome = str(input("Informe seu nome: "))
#     s = int(input("Digite 1 para masculino ou 2 para feminino: "))
#     if s == 1:
#         cm+=1
#     elif s == 2:
#         cf+=1
#     else:
#         print("Sexo inválido!")
#         break
# print("Numero de homens: ",cm," e de mulheres: ",cf)


# qtd = int(input("Digite a quantidade de funcionários: "))
# sal = float(input("Digite o salário: "))
# soma = sal
# maior = sal
# menor = sal
# if sal <= 0:
#     print("Salário inválido!")
# else:
#     for i in range(qtd-1):
#         sal = float(input("Digite o salário: "))
#         if sal <= 0:
#             print("Salário inválido!")
#             break
#         else:
#             if sal > maior:
#                 maior = sal
#             elif sal < menor:
#                 menor = sal
#             soma+=sal
# print("Média dos salários dos ",qtd," funcionários é de: ",soma/qtd)
# print("Maior salário:",maior)
# print("Menor salário:",menor)

# num = int(input("Digite um número: "))
# for i in range(1, 11):
#     print(num," X ", i, " = ",num*i)

# qPares = 0
# qImpares = 0
# num = 0
# while num != -1:
#     num = int(input("Digite um número: "))
#     if num%2 == 0 and num!=0:
#         qPares+=1
#     elif num%2 == 1 and num!=-1:
#         qImpares+=1
# print("Qtd de pares: ",qPares," e qtd de impares: ", qImpares)

# s = 1
# soma = 0
# while s < 6561:
#     s = s * 3
#     print(s)
#     soma+=s
# print("A soma dessa progressão é de ",soma)

# w = 0
# n = int(input("Digite um valor: "))
# for i in range(1,n+1):
#     w = w + 1/i
# print(w)

# t = 0
# k = int(input("Digite um valor: "))
# for i in range(1,101):
#     t = t + (k+i)
# print(t)

# a = 0  
# b = 1 
# n = int(input("Digite a quantidade: "))
# while b < n:  
#     print(b)  
#     b = b + a  
#     a = b - a 

for i in range(50, 151):
    print((i-32)/(9/5))

# c = 1.5
# z = 1.1
# cn = 0
# while c >= z:
#     c = c + 0.02
#     z = z + 0.03
#     cn+= 1
# print("Levou ",cn," anos para Zé ficar mais alto que Chico")

# print("Digite 10 para votar em José da feira")
# print("Digite 20 para votar em Maria Fumaça")
# print("Digite 30 para votar em Chico")
# print("Digite 1 para votar em branco ou 0 para votar nulo!")
# j = 0
# m = 0
# c = 0
# n = 0
# v = 0
# for i in range(10):
#     voto = int(input("Voto: "))
#     if voto == 10:
#         j+=1
#     elif voto == 20:
#         m+=1
#     elif voto == 30:
#         c+=1
#     elif voto == 1 or voto == 0:
#         n+=1
#     else:
#         print("Voto inválido!")
#         v+=1
# print(j," votaram em José da Feira")
# print(m," votaram em Maria Fumaça")
# print(c," votaram em Chico")
# print(n," votaram em branco ou nulo")
# print(v," votaram invalidamente")


# cont2 = 0
# i = 1
# while cont2 < 4:
#     cont1 = 0
#     for f in range(1, i+1):
#         if i%f==0:
#             cont1+=1
#     if cont1==2:
#         print(i)
#         cont2+=1
#     i+=1


# num = 2
# a = 0
# while a < 4:
#     soma = 0
#     for i in range(1, num):
#         if num%i == 0:
#             soma += i
#     if soma == num:
#         print(num)
#         a+=1 
#     num+=1

# print("Digite:")
# print("5 para ótimo")
# print("4 para bom")
# print("3 para regular")
# print("2 para ruim")
# print("1 para péssimo")
# bomRegular=0
# media=0
# c=0
# maiorP=0
# maiorO=0
# maiorR=0
# pe=0
# n = 100
# for i in range(n):
#     ida = int(input("Digite sua idade: "))
#     if ida > 0:
#         op = int(input("Digite sua opinião para o filme: "))
#         if op == 4 or op == 3:
#             bomRegular+=1
#         elif op == 2:
#             media=media+ida
#             c+=1
#             if ida > maiorR:
#                 maiorR = ida
#         elif op == 1:
#             pe+=1
#             if ida > maiorP:
#                 maiorP = ida
#         elif op == 5:
#             if ida > maiorO:
#                 maiorO=ida
#         else:
#             print("Opção inválida!")
#             break
#     else:
#         print("Idade inválida!")
#         break
# print("Quantidade percentual de respostas boas e ruins: ",(bomRegular/n)*100,"%")
# if c > 0:
#     print("A média das idades que responderam ruim: ",(media/c))
# print("Porcentagem de respostas péssimo: ",(pe/n)*100)
# print("Maior idade que marcou péssimo: ",maiorP)
# print("A diferença: ",maiorO-maiorR)



