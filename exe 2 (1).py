numero = 0
contador = 1
Maior = 0
while contador <= 10:
    numero = int(input('Digite 10 valores: '))
    if Maior < numero:
        Maior = numero
    contador +=1
    
print (Maior)