def calcular_area(base,altura):
    Area = base * altura
    return Area

baseDigitada = float(input("digite a altura: "))
AlturaDigitada = float(input("escreva a altura: "))
Area = calcular_area(baseDigitada, AlturaDigitada)
print(f"área de um retângulo: {Area}")
