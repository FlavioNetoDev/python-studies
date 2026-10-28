salario = float(input('Digite o seu salário: '))

if salario >= 1250:
    aumento = 0.10
    final = salario * aumento
    print('O aumento do seu salario de {} começou a passar {}'.format(salario, final + salario))
elif salario < 1250:
    aumento = 0.15
    final = salario * aumento
    print('O aumento do seu salario de {} começou a passar {}'.format(salario, final + salario))