s = 0
c = 0
while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        break
    c += 1 
    s += num
print(f'{c} Numeros foram digitados e a soma entre eles eh {s}')