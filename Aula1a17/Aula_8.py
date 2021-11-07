#nome=str(input('Qual o seu nome? '))
#if nome.upper()=='RODRIGO':#tudo o que estiver dentro do espaço abaixo está dentro da condição
#    print('Que nome lindo')
#    print("{}  e um nome legal".format(nome.upper()))
#print('ola {}'.format(nome))#aqui nao esta dentro da condição
import random
num=random.randint(1,10)
nu=int(input('Digite um numero inteiro de 1 a 10: '))
if nu==num :
    print(' o numero {} foi o mesmo que o computador sorteaou'.format(nu))
else:
    print(' o numero {} não foi o mesmo que o computador sorteaou'.format(nu))
print ('O numero sorteado pelo pc foi {}'.format(num))