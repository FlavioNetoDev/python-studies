from time import sleep
print('-='*20)
print('       \033[4;32;47mAnalisador de Triangulos\033[m')
print('-='*20)
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())
print('\033[7;35;46mProcessando...\033[m')
sleep(3)
s = lado1 + lado2 + lado3 

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Formam um triangulo')
else:
    print('\033[31mNão formam um triangulo')