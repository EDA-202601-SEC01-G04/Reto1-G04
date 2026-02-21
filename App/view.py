import sys
import App.logic as logic 

def new_logic():
    """
        Se crea una instancia del controlador
    """
    catalog = logic.new_logic()
    return catalog
    

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    return logic.load_data(logic.new_logic() , "computer_prices_small.csv" )


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    marca = input("Escriba una marca ")
    req1 = logic.req_1(load_data(control), marca)
    solo_marca, precio, ram, vram, nucleo, año, modelo, tiempo = req1
    mayor,menor = modelo
    print("Número total de computadores de esa marca: " + str(solo_marca)) 
    print("Promedio de precio de estos computadores, precio más bajo y precio más alto: " + str(precio))
    print("Promedio de memoria RAM, menor memoria RAM, mayor memoria RAM: " + str(ram))
    print("Promedio de VRAM, menor memoria VRAM, mayor memoria VRAM: " + str(vram))
    print("Promedio de número de núcleos de CPU, menor número de núcleos, mayor número de núcleo: " + str(nucleo))
    print("Año promedio de lanzamiento, menor año de lanzamiento, mayor año de lanzamiento: " + str(año))
    print("El modelo del computador de mayor precio dentro de la marca indicando su precio respectivo: " + str(mayor["elements"]))
    print("El modelo del computador de menor precio dentro de la marca indicando su precio respectivo: " + str(menor["elements"]))     
    print("Tiempo de la ejecución del requerimiento en milisegundo: " + str(tiempo) )
    


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    cpu_brand = input("Escriba un cpu_brand ")
    gpu_model = input("Escriba un gpu_model ")
    req2 = logic.req_4(load_data(control), cpu_brand, gpu_model)
    tiempo, total, precio, vram, ram, cpu_boost, mayor = req2
    print("Tiempo de la ejecución del requerimiento en milisegundos " + str(tiempo))
    print("Número total de computadores que cumplieron el filtro " + str(total))
    print("Precio promedio " + str(precio))
    print("VRAM promedio " + str(vram))
    print("RAM promedio " + str(ram))
    print("Cpu_boost_ghz promedio " + str(cpu_boost))
    modelo1, marca1, año1, cpu_model1, precio1, modelo2, marca2, año2, cpu_model2, precio2 = mayor
    print("El primer computador costoso tiene modelo: " +str(modelo1)+ ", marca: " +str(marca1)+ " ,año: " +str(año1)+ " ,cpu_model: " +str(cpu_model1)+ " ,precio: " + str(precio1))
    print("El primer computador costoso tiene modelo: " +str(modelo2)+ ", marca: " +str(marca2)+ " ,año: " +str(año2)+ " ,cpu_model: " +str(cpu_model2)+ " ,precio: " + str(precio2))
    
    
    
def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
