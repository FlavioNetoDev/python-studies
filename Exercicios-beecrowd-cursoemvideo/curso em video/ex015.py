dias = int(input('Quantos dias alugados?: '))
km = float(input('Quantos km rodados? '))
dia = 60
kms = 0.15
valor = (dias * dia) + (km * kms)

print('Valor a pagar {:.2f} '.format(valor))

