def Dolar (num):
    return num*5;

def porcentagem (num, porc):
    ft = porc/100
    return num*ft

def Info(num, porc):
    print('Dados:')
    print(f'{num} equivale a {Dolar(num)} dolares')
    print(f'{porc}% de {num} equivale a {porcentagem(num,porc)}')