def verificar_par(numero):
     if numero % 2 == 0:
          return True
     else:
        return False

Numero = int(input("Digite o numero:"))
Resultado = verificar_par(Numero)
print(Resultado)