num = int(input("Digite o número da volta: "))
tempo = float(input("Digite o tempo: "))
melhor = tempo
volta = num
count = tempo
count1 = 1
if num == 0:
    print("Fim")
else:
    while num!=0:
        num = int(input("Digite o número da volta: "))
        if num == 0:
            break
        else:
            tempo = int(input("Digite o tempo: "))
            if tempo < melhor:
                melhor = tempo
                volta = num
            count+=tempo
            count1+=1
    print("O melhor tempo foi de: ",melhor, " na ",volta, "volta")
    print("O tempo médio é de ",(count/count1) )

        
