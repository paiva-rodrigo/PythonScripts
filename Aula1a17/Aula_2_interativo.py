n11=input('Digite um numero:')
print(type(n11))
n12=input('Digite um numero:')
print(type(n12))
print('a soma vale',n11+n12)

n21=int(input('Digite um numero:'))
print(type(n21))
n22=int(input('Digite um numero:'))
print(type(n22))
print('a soma vale',n21+n22)
#aqui foi mostrado como os numers podem ser salvados de forma diferente,sendo que
#e salvado automaticamente como str(string) como no caso 1

n=n21+n22
print('A soma entre {},{} e vale: {}'.format(n11,n12,n))
#forma de escrever .format

n3=input('Digite um algo:')
print(n3.isnumeric())
 #ve se o que foi digitdo e um numero

