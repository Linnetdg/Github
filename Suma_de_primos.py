maximo = int(input("Suma de los números primos hasta el: "))
suma_total = 0
if maximo >= 2:
    suma_total += 2
numero = 3
while numero <= maximo:
    limite_divisor = int(numero**0.5) + 1
    
    for divisor in range(2, limite_divisor):
        if numero % divisor == 0:
            break  
    else:
        suma_total += numero
        
    numero += 2

print("La suma de los números primos hasta el", maximo, "es:", suma_total)

 git config --global user.email "you@example.com"
  git config --global user.name "Your Name"