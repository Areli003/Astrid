frutas = ["manzana", "pera", "uva"]

for fruta in frutas:
    print(fruta)

for i in range(5):
    print(i)
        
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador = contador + 1
    
numero = int(input("Ingrese un numero: "))
for i in range(11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")