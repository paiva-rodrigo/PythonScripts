#trabalhando com cores no terminal
#codigo ansi
#codigo padra de cor \033[style;text;back m
#style            text        back
#0 none          30 branco     40 mesmas cores anteriores
#1 bold(negrito) 31 vermelho   41
#4 underline     32 verde      42
#7 negative      33 amarelo    43
#                34 azul       44
#                35 roxo       45
#                36 verde      46
#                37 cinza      47
#print('\033[1;30;45m olá mundo\033[m')#\033[m no final serve para fazer com que nao colora ate o final da linha, apenas ate a ulyima letra
a=5
b=10
#print("Os numeros sao \033[1;31;47m{}\033[m e \033[1;31;47m{}\033[m".format(a,b))
nome='Rodrigo'
#print('Prazer em te conhecer {}{}{}!!!'.format('\033[2;34;40m',nome,'\033[m'))

#Aqui outra forma de progamar
cores={ 'azul':'\033[1;34m',
        'amarelo':'\033[1;33m',
        'verde':'\033[1:32',
        'finaliza':'\033[m' }
print('Meu nome é {}{}{}'.format(cores['azul'],nome,cores['finaliza']))
print("Caneta {}{}{},{}{}{} Caneta".format(cores['azul'],'Azul',cores['finaliza'],cores['azul'],'Azul',cores['finaliza']))

print('\033[1;37m Teste Final\033[m')