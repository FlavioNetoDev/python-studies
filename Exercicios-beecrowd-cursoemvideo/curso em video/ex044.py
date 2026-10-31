preço = float(input('Qual o preço do produto? '))
print('FORMAS DE PAGAMENTO')
print('1 - A VISTA \n2 - CARTÃO DE CRÉDITO')
forma = int(input('Digite o numero relacionado as formas '))

if forma == 1:
    desconto = preço * 0.10
    aplicado = preço - desconto
    print('Preço com desconto {}'.format(aplicado))
elif forma == 2:
    print('1 - PARA PARCELAR \n2 - PARA PAGARA A VISTA')
    parcelando = int(input('Digite um numero relacionado as formas '))
    if parcelando == 2:
        desconto = preço * 0.05
        aplicado = preço - desconto
        print('Preço com o desconto a vista {}'.format(aplicado))
    elif parcelando == 1:
        parcelas = int(input('Em quantas vezes deseja parcelar? '))
        if parcelas == 2:
            valor_parcela = preço / parcelas
            print('Preço parcelado em ate 2x {}'.format(valor_parcela))
        elif parcelas >= 3:
            juros = preço * 0.20
            aplicado = preço + juros
            valor_parcela = aplicado / parcelas
            print('Preço parcelado em {}x, {}'.format(parcelas, valor_parcela))
        elif parcelas <= 0:
            print('Escolha um valor positivo de parcelas.')
else:
    print('Escolha uma forma de pagamento acima')
    exit()