largura = float(input('Qual a largura da parede? '))
altura =  float(input('Qual a altura da parede? '))

area = largura * altura
tinta = area / 2

print('A parede tem a dimensao de {} x {} e sua area e de {:.2f} m2.'.format(largura, altura, area))
print('A quantidade de tinta que o Sr(a) vai precisar para pintar a parede e de {} l.'.format(tinta))


