nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segundo nota: '))
nota3 =  float(input('Digite a terceiro nota: '))
media = (nota1 + nota2 + nota3) / 3
if media > 7:
    print ('Parabéns {} você passou'.format (media, nome))
if media <= 7 and media >= 5:
    print ('{} você ficou com a média'.format (media, nome))
if media < 5:
    print ('{} ESTÁ REPROVADO'.format (media))