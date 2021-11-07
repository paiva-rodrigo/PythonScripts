#help(print) ira mostrar as informações desse comando
#print(input.__doc__) outra forma de fazer com que informações sobre o comando sejam dadas

#existe uma forma de fazer com que se escreva um manual dentro de uma função
#def contador (i, f, c):
#    """
#    --->Aqui sao definidos os comandos de orientação.
#    :i para inicio.
#    :f para final.
#    :c para contador.
#    """
#    while i <= f:
#       print(i,end=' ')
#        i += c
#
#print('Inicio da função')
#i = int(input('Digite o inicio: '))
#f = int(input('Digite o final: '))
#c = int(input('Digite o contador: '))
#contador(i, f, c)

# o python tem uma propiedade que muitas outras linguagens nao   tem
# no caso o python criou outra variável n1
def dentro():
    n1 = 4
    print(n1)
n1=5
print(n1)
dentro()







