''''- La jornada de trabajo es de 48 horas (no se pueden trabajar menos horas), solicitar las horas trabajadas y, con el valor por hora y el valor por hora extra, debe mostrar:.
 * Horas extras trabajadas (si las hubiera)
 * Mostrar el pago total de horas extras (si las hubiera).
 * Mostrar el pago total de la jornada'''
vh = 15 #$(valor de pago por hora normal)
he = 20 #$(valor de pago por hora extra)
ht=48;
horas= int(input("Ingrese las horas total trabajadas: "));
if horas >= ht:
    vh = ht *vh;
    ht= horas - ht;
    print("total de horas extras: ", ht ,"horas")
    print("el pago de la jornada es: $",vh);
    he =(horas-ht)*he
    print("el pago de las horas extras son: $",he);
    print("el pago total de la jornada es : $",vh + he);
else:
    print("se debe trabajar mas de 48hs");
print("segunda parte")
horas= int(input("ingrese horas trabajadas: "));
if horas>=ht:
    vh = ht *vh
    he = (horas -ht)*he
else:
    vh = horas * vh
print("el pago de la jornada: $",vh)
print("el pago de horas extras: $", he);
print("el pago total de la jornada es : $", vh + he)


    
    
    
    
    
