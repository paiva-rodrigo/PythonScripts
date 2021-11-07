#filme = {'titulo' : 'star wars',
#     'ano' : '1977',
#     'diretor' : 'george lucas'
#}
#isso é um dicionário e todos os valores são salvos
#print(filme.values()) mostra os valores armazenados dentro dos keys no caso satar wars 1977 e george lucas
#print(filme.keys()) mostra as keys ano titulo e diretor
#print(filme.items()) mostra keys+ values
#for k,v in filme.items():
#     print(f'O {k} e {v}')

#pessoas = {
#     'nome' : 'rodrigo',
#     'idade' : '19',
#     'Naturalidade' : 'Piranga'
#}
#print(pessoas)
#print(pessoas['nome'])#tava mostrando o que esta armazenado em nome : rodrigo
#pessoas['nome'] = 'Rods Reis'
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos  de idade')

#estado = dict()
#brasil = list()
#for c in range(0,2):
#     estado['uf']=str(input('Qual a sigla do seu estado?'))
#     estado['sigla']=str(input('Digite agora o nome:'))
#     brasil.append(estado.copy())
#for e in brasil:
#     for k,v in e.items():
#          print(f'O campo {k} tem valor {v}')
#      for v in e.values():
#          print(v,end=' ')
#     print()

#nota = dict()
#nota['nome'] = str(input('Qual seu nome: '))
#nota['idade'] = str(input('Qual sua idade: '))
#print(f'O nome e {nota["nome"]} e a nota vale {nota["idade"]}')

#from random import randint
#sorteio ={'Jog1': randint(1, 6),
#          'Jog2': randint(1, 6),
#          'Jog3': randint(1, 6)
#         }
#rank = list()
#
#
#print(rank)
#from  datetime import datetime
#Carteira = dict()
#Carteira['nome'] = str(input('Digite seu nome: '))
#Carteira['Ano de nascimento'] = int(input('Digite sua data de nascimento: '))
#Carteira['salário'] = int(input('Digite seu salário: '))
#Carteira['Idade'] = datetime.now().year-Carteira['Ano de nascimento']
#Carteira['Ano de Contraação'] = int(input('Digite seu ano de contratação: '))
#print(Carteira)

#dados = dict()
#part = list()
#dados['nome'] = str(input('Digite o seu nome: '))
#dados['partidas'] = int(input('Quantas partidas ele jogou?'))
#for c in range(0, dados['partidas']):
#    part.append(int(input('Qual numero de gols na {} partida? '.format(c+1))))
#total=sum(part)
#dados['Gols'] = part[:]
#dados['media de gols']=total/dados['partidas']
#print(dados)
id=0
mul=0
quant=0
dadoidade=list()
dadonome=list()
dadosexo=list()
result=dict()
while (True):
    seq=str(input('Deseja continuar: '))
    if seq.lower() == 'n':
        break
    else:
       dadonome.append(str(input('Qual seu nome: ')))
       idade= int(input('Qual seu idade:'))
       id+=idade
       dadoidade.append(idade)
       sexo=str(input('Qual seu sexo: '))
       if sexo.lower()=='f':
           mul+=1
       dadosexo.append(sexo)
       quant+=1
       result['Nome']=dadonome[:]
       result['Idade'] = dadoidade[:]
       result['Sexo'] = dadosexo[:]
print(f'Total mulheres {mul}')
print(f'Media das idades {id/quant}')
print(f'Total mulheres {result}')




