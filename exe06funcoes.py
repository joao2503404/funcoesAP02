def calcular_media(notas):
    soma = sum(notas) / len(notas)
    return soma

minha_lista = [ 30, 60, 90]
Resultado = calcular_media(minha_lista)
print (f"{Resultado:.2f}")
