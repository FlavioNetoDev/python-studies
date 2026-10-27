ano = int(input('Digite o ano: '))

if (ano % 4) == 0:
    print('Esse ano {} é bissexto'.format(ano))
elif ano % 4 == 0 and ano // 400:
    print('Esse ano {} é bissexto'.format(ano))
else:
    print('Esse ano {} não é bissexto'.format(ano))