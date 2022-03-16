# Média aritimética, totalmente realizado por mim:
nome = str(input('Olá, digite seu nome:'))
print('Legal, {}, Vamos para a média das notas?'.format(nome))
n1 = float(input('Digite a sua nota do primeiro bimestre:'))
n2 = float(input('Digite a sua nota do segundo bimestre:'))
n3 = float(input('Digite a sua nota do terceiro bimestre:'))
n4 = float(input('Digite a sua nota do quarto bimestre:'))
media = ((n1 + n2 + n3 + n4) / 4)
print('Sua média é {:.2f}'.format(media))
if media >= 6.0:
    print('Você está aprovado(a), Parabéns!!!')
else:
    print('Você está reprovado(a), KAKAKAKAKA!!! SE FODEU!!!')
