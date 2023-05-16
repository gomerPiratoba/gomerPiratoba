- from datetime import*
nombreParqueadero="Parqueadero los Almendros"
print (nombreParqueadero)
servicio = "Servicio parqueo las 24 horas"
print (servicio)
#Variables para los precios
tarifaHoraMoto=12000
tarifaDiaMoto = 24000
tarifaHoraCarro = 20000
tarifaDiaCarro = 40000
#Variabkes para  llevar el tiempo
formato = '%Y-%m-%d %H:%M:%S'
print('C para carros')
print('M para motos')
opcion = input('ingrese c o m según el caso:')
if opcion=='M' or opcion=='m':
    hora_ingresoM=input('Hora de ingreso:')
    hora_salidaM=input('Hora de salida:')
    tiempo_in=datetime.strptime(hora_ingresoM,formato)
    tiempo_o=datetime.strptime(hora_salidaM,formato)
    tiempo_p = tiempo_o - tiempo_in    
    minutos=tiempo_p.seconds//60
    horas=minutos//60
    minutoF=minutos%60
    dia = tiempo_p.days
    if horas <=12 and dia<1:
        valorApagar=horas*tarifaHoraMoto+minutoF*50
        print("El valor a pagar es:", valorApagar)
    else:
        valorApagar=tarifaDiaMoto*dia
        print("El valor a pagar es:", valorApagar)
if opcion=='C' or opcion=='c':
    hora_ingresoC=input('Hora de ingreso:')
    hora_salidaC=input('Hora de salida:')
    tiempo_in=datetime.strptime(hora_ingresoC,formato)
    tiempo_o=datetime.strptime(hora_salidaC,formato)
    tiempo_p = tiempo_o - tiempo_in    
    minutos=tiempo_p.seconds//60
    horas=minutos//60
    minutoF=minutos%60
    dia = tiempo_p.days
    if horas <=12 and dia<1:
        valorApagar=horas*tarifaHoraCarro+minutoF*50
        print("El valor a pagar es:", valorApagar)
    else:
        valorApagar=tarifaDiaCarro*dia
        print("El valor a pagar es:", valorApagar)
