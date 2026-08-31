'''
#Exercício 1
umCent=float((input('Moedas de um centavo: ')or '0'.replace(",",".")))
cincoCent=float((input('Moedas de cinco centavos: ')or '0'.replace(',','.')))
dezCent=float((input('Moedas de dez centavos: ')or '0'.replace(',','.')))
vintecincoCent=float((input('Moedas de vinte e cinco centavos: ')or '0'.replace(',','.'))) 
cinquentaCent=float((input('Moedas de cinquenta centavos: ')or '0'.replace(',','.')))
umReal=float((input('Moedas de um real: ')or '0'.replace(',','.')))
total = (umCent * 0.01) + (cincoCent * 0.05) + (dezCent * 0.10) + (vintecincoCent * 0.25) + (cinquentaCent * 0.50) + (umReal * 1.00)
valorUmCent = umCent * 0.01
valorCincoCent = cincoCent * 0.05
valorDezCent = dezCent * 0.10
valorVinteCincoCent = vintecincoCent * 0.25
valorCinquentaCent = cinquentaCent * 0.50
valorUmReal = umReal * 1.00
print("O valor total economizado é: R$", round(total, 2))
print("Valor economizado com moedas de 1 centavo: R$", round(valorUmCent, 2))
print("Valor economizado com moedas de 5 centavos: R$", round(valorCincoCent, 2))
print("Valor economizado com moedas de 10 centavos: R$", round(valorDezCent, 2))
print("Valor economizado com moedas de 25 centavos: R$", round(valorVinteCincoCent, 2))
print("Valor economizado com moedas de 50 centavos: R$", round(valorCinquentaCent, 2))
print("Valor economizado com moedas de 1 real: R$", round(valorUmReal, 2))

#Exercício 2
totalrefresco=float(input('Digite a qunatidade de refresco desejada: '))
litrosagua= totalrefresco * 0.8
litrossuco = totalrefresco * 0.2
print('Para fazer',totalrefresco,'litros de suco são necessários:',litrosagua,'litros de água, e',litrossuco,'litros de suco.')

#Exercício 3
precoProduto=float(input('Digite o valor do produto: '))
desconto=float(precoProduto*0.10)
print('Com dez por cento de desconto, o valor do produto será',precoProduto-desconto)

#Exercício 4
fixo=float(input('Digite o salário fixo: '))
comissao=float(0.4*fixo)
print('Comissão:{}\nSalário final:{}'.format(comissao,fixo+comissao))

#Exercício 5
peso=float(input('Qual é seu peso?: '))
gordo=0.15*peso
magro=0.20*peso
print('Se engordar 15%, novo peso: {:.1f}kg,\nSe emagrecer 20%, novo peso: {:.1f}kg.'.format(gordo+peso,peso-magro))

#Exercício 6
salario=float(input('Valor do salário do funcionário: '))
salarioMinimo=float(input('Valor do salário mínimo: '))
qtdSalarioMinimo=salario/salarioMinimo
print(f'O funionário que recebe R${salario}, recebe {qtdSalarioMinimo} salários mínimos.')

#Exercício 7
num=float(input('Digite um número: '))
print('{}x1={}\n{}x2={}\n{}x3={}\n{}x4={}\n{}x5={}\n{}x6={}\n{}x7={}\n{}x8={}\n{}x9={}\n{}x10={}'.format(num,num*1,num,num*2,num,num*3,num,num*4,num,num*5,num,num*6,num,num*7,num,num*8,num,num*9,num,num*10))

#Exercício 8
nasc=int(input('Digite o ano do nascimento: '))
atual=int(input('Digite o ano atual: '))
print('Idade em anos:{}\nIdade em meses:{}\nIdade em dias:{}\nIdade em semanas:{}'.format(atual-nasc,(atual-nasc)*12,(atual-nasc)*365,((atual-nasc)*365)//7))

#Exercício 9
slr=float(input('Digite seu salário: '))
c1=float(200+(200*0.02))
c2=float(120+(120*0.02))
print('Você possui contas atrasadas.\nConta 1 valor com juros:R${}\nConta 2 valor com juros:R${}'.format(c1,c2))
print(f'Restará {slr-c1-c2} de seu salário.')
'''