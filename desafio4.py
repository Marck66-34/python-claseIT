from operator import length_hint


matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]];
fila= int(input("ingrese fila"));
columna= int(input("ingrese columna: "));
if( fila == 0 or fila ==1) and(columna >= 0 and columna <=2):
    print(matriz[fila][columna])
else:
    print("columna incorrecta");
