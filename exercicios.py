'''
lata350=int(input('Latas 350ml: '))
garrafa600=int(input('Garrafa 600ml: '))
garrafa2lts=int(input('Garrafa de 2lts: '))

litroslata350=lata350*0.350
litrosgarrafa600=garrafa600*0.600
litrosgarrafa2lts=garrafa2lts*2

totallitros= litrosgarrafa2lts + litrosgarrafa600 + litroslata350
print(totallitros)


#Sistema média escolar
nome=str(input('Nome do aluno: '))
a1=float(input('Nota Avaliação 1: '))
a2=float(input('Nota Avaliação 2: '))
media=(a1+a2)/2
if media >= 7 and media <=10:     #verdadeiro ou falso
    print('Aprovado!')
elif media >=4 and media <7:      # se if falso, entra o elif
    print('Recuperação!')
elif media >=0 and media <4:      # quantos for necessário
    print('Reprovado!')
else:                              # caso nenhuma condição for atendida
    print('Média inválida!')


#IMC mede se a pessoa esta acima, dentro ou abaixo do peso.
#O sistema deve solicitar par ao usuario: Altura,peso.
#O sistema deve calcular o IMC = peso / altura².

peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))
imc=peso / altura ** 2
print('IMC:{:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif imc >=18.5 and imc <25:
    print('Peso ideal!')
elif imc > 25:
    print('Acima do peso!')
'''