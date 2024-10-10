#biblioteca
from math import sqrt
#funcao que caucula

def calcular_hipotenusa(c1,c2):
    h = sqrt((c1**2) + (c2**2))
    return h 
#progranma principal
print("CAUCULAR HIPOTENUSA")

#USUARIO IMFORMAR VALOR DO CATETO
c1 = float(input("imforme o valor do 1º cateto:").replace(",","."))
c2 = float(input("imforme o valor do 2º cateto:").replace(",","."))

#exibe o valor da H na tela

print(f"o valor da hipotenusa e{caucular_hipotenusa(c1,c2)}.")