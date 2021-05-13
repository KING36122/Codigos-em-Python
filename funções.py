# def soma(a,b):
#     c = a + b
#     return c

# x = int(input("Digite: "))
# y = int(input("Digite: "))
# a = soma(x,y)
# print(a)

def maiorIdade(idade):
    if idade >= 18:
        return True
    else:
        return False

id = int(input("Digite sua idade: "))
a = maiorIdade(id)
if a == True:
    print("Maior")
else:
    print("Menor")