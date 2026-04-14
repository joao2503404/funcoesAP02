def maior_valor(a,b):
    if a > b:
        return a
    else:
        return b

A = int(input("digite o primeiro valor: "))
B = int(input("digite o segundo valor: "))
Maior = maior_valor(A,B)
print(f"O maior numero e o {Maior}")