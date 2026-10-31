print('======EMPRESTIMO======')
valor = float(input('Valor da casa?: '))
salario = float(input('Salario do comprador?: '))
anos = int(input('Quantos anos de financiamento?: '))
limite = salario * 0.30
meses = anos * 12
prestação = valor / meses
print('Pra pagar uma casa de {:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestação))
if prestação > limite:
    print('Emprestimo negado, a prestação ultrapassa 30% do salario')
else:
    print('Emprestimo Aceito')