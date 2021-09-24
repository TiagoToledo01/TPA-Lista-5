contador=1
resultado=1
fatorial = int(input('Digite um número e mostraremos o fatorial:  ') )
while contador <= fatorial:
    resultado *= contador
    contador += 1
print('resultado do fatorial de {} é {}'.format (fatorial, resultado))