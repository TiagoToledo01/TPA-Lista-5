nascido = 0
contador = 1
total = 0
while contador <= 10:
    contador += 1
    nascido = int(input('Em que ano você nasceu: '))
    maior = 2021 - nascido
    if maior >= 18:
        total += 1
print ('{} São maiores de idade'.format (total))