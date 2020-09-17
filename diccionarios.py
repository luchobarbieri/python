def run():
    poblacion_paises = {
        'Argentina': 44890123,
        'Brasil': 1241241414,
        'colombia': 30678123,
    }
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')



if __name__ == "__main__":
    run()