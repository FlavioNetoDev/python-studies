preco = float(input('Qual e o preco do produto? R$'))

desconto = preco * 0.05
novopreco = preco - desconto

print('O produto que antes custava {} agora esta custando {} com o nosso cupom de desconto!'.format(preco, novopreco))
