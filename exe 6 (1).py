p1 = int(input('Digite o preço do primeiro produto: '))
p2 = int(input('Digite o preço do segundo número: '))
desconto1= ((p1 * 8) / 100) - p1
desconto2= ((p2 * 11) / 100) - p2
resultado= (desconto1 + desconto2) *-1
print ('Com o desconto de 8% e  11%  o total vai ser de {}'.format (resultado))