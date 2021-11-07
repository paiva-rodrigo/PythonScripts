#comando de condição no pytho sao eles {if  else  elif(else if)}
#nom=str(input('Qual é o seu nome? '))
#if nom.lower()=='rodrigo':
#    print('Nome melhor que iranildo')
#elif nom.lower()=='carine':
#    print('seu nome ia ser priscila e priscila e nome de cachorro')
#else:
#    print("Nao sei seu nome")
num=int(input('Digite um nuero na base 10: '))
n=int(input('''quer passar esse numero para"
     [1] binaria
      [2] octal
      [3] hexadecimal
      '''))
if n==1:
   print('o numero vale \033[1;33m{}\033[m'.format(bin(num)))
elif n==2:
   print('o numero vale \033[1;33m{}\033[m'.format(oct(num)))
elif n==3:
   print('o numero vale \033[1;33m{}\033[m'.format(hex(num)))


