lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Triangulo', end=' ')

    if lado1 == lado2 and lado2 == lado3:
        print('Equilatero')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Isóceles')
    else:
        print('Escaleno')
else:
    print('Não é um triangulo')