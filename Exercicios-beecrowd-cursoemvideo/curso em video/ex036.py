print('======EMPRESTIMO======')
valor = float(input('Qual o valor da casa que deseja?: '))
salario = float(input('Qual o seu salario? '))
anos = int(input('Em quantos anos vc vai pagar? '))
limite = salario * 0.30
meses = anos * 12
prestação = valor / meses
if prestação > limite:
    print('Emprestimo negado, seu salario não ultrapassa a prestação mensal')
else:
    print('Emprestimo Aceito')