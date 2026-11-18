t = int(input())
contador = 0
resposta = input().split()
for c in resposta:
    c = int(c)
    if c == t:
        contador += 1
print(contador)