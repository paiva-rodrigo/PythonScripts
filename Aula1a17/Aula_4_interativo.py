nome='rodrigo'
print('prazer em te conhecer {:20}!'.format(nome))
#gasta 20 espaos pra escrever
print('\nprazer em te conhecer {:>20}!'.format(nome))
#alinhamento a direita
print('\nprazer em te conhecer {:<20}!'.format(nome))
#alinhamento a esquerda
print('\nprazer em te conhecer {:^20}!'.format(nome))
#alinhamento ao centro
print('\nprazer em te conhecer {:=^20}!'.format(nome))

n1=int(input('Digite um numero: '))
n2=int(input('Digite um numero: '))
print('a soma vale {},potencia {},divisao inteira {},diferença {},divisao {:.3f}'.format(n1+n2,n1**n2,n1//n2,n1-n2,n1/n2))
#calcular a quantia de casas gastas serviu no caso para ver quantas casas apos a virgula usar
print('a soma vale {},potencia {},divisao inteira {}'.format(n1+n2,n1**n2,n1//n2),end='')
#end='' usado para imendar linhas
print(' diferença {},divisao {:.3f}'.format(n1-n2,n1/n2))     

#exercicio
#print(' o valor da raiz quadrada do numero {} e {} seu antecessor vale {}'.format(n1,n1**(1/2),n1-1)) 
