#agora vamos trabalhar com lidtas que são declaradas da seguinte forma
#lista=['arror','feijão','batata']
#print (lista)
#lista.insert(0,'linguiça') insere linguiça antes do numero que esta na posição 0
#del lista[2] apaga o item da posição dois
#lista.pop(2apaga o item da posição dois)
#lista.remove('feijão') remove o item feijão
#print(lista)

#listanumerica= [5, 4, 3, 2, 1, 99]
#listanumerica[4]=88
#listanumerica.append(98)
#listanumerica.pop(4) retira o numero entre parenteses
#listanumerica.append(101)
#print(listanumerica)
#print(f'Essa lista tem {len(listanumerica)} numeros')
#for c, v in enumerate(listanumerica): enumerate consegue fazer um contador e mostrar o valor
 #   print(f'o valor {v} esta na posição {c}')
#print("cheguei ao final da lista")

#a=[2,3,4,5]
#b=a
#b[2]=9 # quando se liga uma lista a outra quqlquer mudança em uma afeta a outra
#print(f"A lista b vale {b} enquanto a a vale {a}")

#lista=[]
#for cont in range(0,5):
#    lista.append(int(input('Digite um numero: ')))
#    if cont==0:
#        men=lista[0]
#        mai=lista[0]
#    elif mai>=lista[cont]:
#        mai=lista[cont]
#    elif men<=lista[cont]:
#        men=lista[cont]
#print(f'O maior numero e {men}')
#print(f'O menor numero e {mai}')
#print(lista)
#lista=[]
#lista.append(int(input('Digite um numero para ser adicionado a lista:')))
#resp=str(input('Quer continuar?'))
#while resp.upper() != 'N':
#    lista.append(int(input('Digite um numero para ser adicionado a lista:')))
#    resp = str(input('Quer continuar?'))
#print(lista)
#print(lista.sort())

lista=[]
for cont in range(0,5):
    lista.append(int(input('Digite um numero: ')))
    if cont !=0 and lista[cont-1]>=lista[cont]:
         mai =lista[cont-1]
         lista[cont-1]=lista[cont]
         lista[cont]=mai
print(lista)

