#sumar una lista de numeros
numeros =[1,2,4];
suma=0;
for numero in numeros:
    suma = suma + numero;
print("la suma es:",suma);

#multiplicar una lista
multiplicar=1;
for numero in numeros:
    multiplicar= multiplicar*numero;
print("la multiplicacion es ", multiplicar)

#busca el mayor
mayor = numeros [0]
for numero in numeros:
    if numero > mayor:
        mayor= numero;
print("el mayor es: ",mayor)
