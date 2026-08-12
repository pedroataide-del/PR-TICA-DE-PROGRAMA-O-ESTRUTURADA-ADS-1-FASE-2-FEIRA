'''
nome=str(input('Digite seu nome: '))
idade=int(input('Digite sua idade: '))
altura=str(input('Digite sua altura '))
peso=float(input('Digite seu peso: '))
n=int(2026 - idade)
print('Você nasceu do ano de', n,'.')
'''
'''
l=float(input('Qual a largura da parede?: '))
a=float(input('Qual a altura da parede?: '))
ar=float(l*a)
print('Para pintar uma área de {}m² são necessários {} litros de tinta.'.format(ar,ar/2))
'''
'''
p=float(input('Digite o preço do produto: '))
print('Você ganhou 5% de desconto! compre agora por somente {:.2f} reais!'.format(p-p*0.05))
'''
s=float(input('Digite seu salário: '))
print('Com aumento de 15% seu salário agora é de {:.2f} reais.'.format(s+s*(15/100)))
