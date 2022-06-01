''' Crear un programa que permita insertar una matriz, y que ésta sea almacenada como una lista de
Python(que a su vez contendrá otras listas, tal como se vió en el material del alumno). '''
''' matriz = [[53, 61, 77],
         [4, 10, 64],
         [101, 58, 54]] '''
resultado= [];

f = int(input("Ingrese n° de Fila: "));#pido al usuario que ingrese los datos
c = int(input("Ingrese n° de Columna: "))
for n_f in range(0, f):
    resultado.append([]);
    for n_c in range(0, c):
        elemento = input("ingrese el valor para la posicion["+str(n_f)+ "]["+ str(n_c)+"]")

        resultado[n_f].append(elemento);
print ("la matriz ingresada es: ")
print(resultado);