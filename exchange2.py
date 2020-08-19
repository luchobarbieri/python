menu = """
Bienvenido al conversor de monedas 💸
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion """


opcion = input(menu)

if opcion == '1':
    pesos = input ("Cuantos pesos colombianos tiene: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tiene $ " + dolares + " dolares")
elif opcion == '2':
    pesos = input ("Cuantos pesos argentinos tiene: ")
    pesos = float(pesos)
    valor_dolar = 140
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tiene $ " + dolares + " dolares")
elif opcion == '3':
    pesos = input ("Cuantos pesos mexicanos tiene: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tiene $ " + dolares + " dolares")
else:
    print("Ingrese un valor correcto por favor")









