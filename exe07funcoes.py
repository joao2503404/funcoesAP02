def Conversor_Temperatura(Celsius):
    fahrenheit = (Celsius * 1.8) + 32
    return fahrenheit


graus = float(input("Digite a Temperatura em Celsius: "))
Resultado = Conversor_Temperatura(graus)
print (f"{Resultado:.2f} °F")