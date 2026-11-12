sexo = input('Digite seu sexo: ').strip().upper()
while sexo not in ['F', 'M']:
    sexo = input('Digite um sexo correspondente a F ou M: ').strip().upper()
print(f'Sexo {sexo} registrado com sucesso')