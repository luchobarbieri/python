Bienvenida = input("Ingresa tu nombre: ")
print ("Hola " + Bienvenida)
accion = int(input(''' 
Que operacion desea realizar?
[1] Convertir mi moneda local a dolares
[2] Convertir dolares a mi moneda local
[3] Salir
Selecciona: '''))



if accion == 1:
    moneda = int(input('''
Cual es tu moneda Local?
[1] Peso Argentino
[2] Peso Mexicano
[3] Peso Colombiano
[4] Ninguna de las anteriores
Selecciona: '''))

elif accion == 2:
    money = int(input('''
Cual es tu moneda local?
[1] Peso argentino
[2] Peso Mexicano
[3] Peso Colombiano
[4] Ninguna de las anteriores
Selecciona: '''))

elif accion == 3:
    print("Hasta luego: " + Bienvenida)


if moneda == 1:
    argentino = input("Ingresa la cantidad de pesos Argentinos: ")
    argentino = float(argentino)
    r_c = argentino / 140
    r_c = round(r_c, 2)
    print("Usted tiene: "  + str(r_c) + " dolares")
if moneda == 2:
    mexicano = input("Ingresa la cantidad de pesos Mexicanos: ")
    mexicano = float(mexicano)
    r_c = mexicano / 50
    r_c = round(r_c, 2)
    print("Usted tiene: " + str(r_c) + " dolares")
if moneda == 3:
    colombiano = input("Ingresa la cantidad de pesos Colombianos: ")
    colombiano = float(colombiano)
    r_c = colombiano / 3650
    r_c = round(r_c, 2)
    print("Usted tiene: " + str(r_c) + " dolares")
if moneda == 4:
    print("Hasta luego: " + Bienvenida)








   








    






    
pesos = input ("Cuantos pesos colombianos tiene: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tiene $ " + dolares + " dolares")
    

  




    
   