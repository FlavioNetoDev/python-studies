peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura em centimetros? ')) / 100
imc = peso / (altura * altura)

if imc <= 18.5:
    print('IMC de {:.2f}, Abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    ('IMC de {:.2f}, Peso ideal'.format(imc))
elif imc >= 25 and imc <= 30:
    print('IMC de {:.2f}, Sobrepeso'.format(imc))
elif imc >= 30 and imc <= 40:
    print('IMC de {:.2f}, Obesidade'.format(imc))
else:
    print('IMC de {:.2f}, Obesidade mórbida'.format(imc))