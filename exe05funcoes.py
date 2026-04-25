def Media_Aritmetica(n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma / 3
    return media




nt1 = int(input("escreva a primeira nota: "))
nt2 = int(input("escreva a segunda nota: "))
nt3 = int(input("escreva a terceira nota: "))

Resultado = Media_Aritmetica(nt1, nt2, nt3)
print(f"{Resultado:.2f}")