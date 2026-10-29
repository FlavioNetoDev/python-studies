cores = {'limpa':'\033[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[7:30m'}

distancia = int(input('Quantos kms é a sua viagem?: '))

if distancia >= 200:
    preco = 0.45
    print('Sua viagem vai custar R$ {}{:.2f}'.format(cores['amarelo'], preco * distancia))
else:
    preco = 0.50
    print('Sua viagem vai custar {} R$ {}{:.2f}'.format(cores['azul'], cores['amarelo'], preco * distancia))