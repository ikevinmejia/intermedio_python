def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firtsname": "Kevin", "lastname": "Mejía"}


    super_list=[
        {"firtsname": "Kevin", "lastname": "Mejía"},
        {"firtsname": "Migue", "lastname": "Torres"},
        {"firtsname": "Pepe", "lastname": "Rodelo"},
        {"firtsname": "susana", "lastname": "Martinez"},
        {"firtsname": "José", "lastname": "Mejía"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_num": [1.1,4.5,6.43]
    }

    # Cilo for en un diccionario de listas
    for key, value in  super_dict.items():
        print(key, "-", value)

    #Ciclo for en una lista de diccionarios
    for i in super_list:
        print(i["firtsname"], "-", i["lastname"])
if __name__ == "__main__":
    run()