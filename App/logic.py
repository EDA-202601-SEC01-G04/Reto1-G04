import time
import csv
import os
csv.field_size_limit(2147483647)
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'


#CON ARRAY_LIST
def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos 
    """
    catalog = {
        'device_type': None,
        'brand': None,
        'model': None,
        'release_year': None,
        'os': None,
        'form_factor': None, 
        'cpu_brand': None,
        'cpu_model': None,
        'cpu_tier': None,
        'cpu_cores': None,
        'cpu_threads': None,
        'cpu_base_ghz': None,
        'cpu_boost_ghz': None,
        'gpu_brand': None,
        'gpu_model': None,
        'gpu_tier': None,
        'vram_gb': None,
        'ram_gb': None, 
        'storage_type' : None, 
        'storage_gb' : None, 
        'storage_drive_count': None,
        'display_type' : None,
        'display_size_in': None,
        'resolution' : None,
        'refresh_hz' : None,
        'battery_wh' : None,
        'charger_watts' : None, 
        'psu_watts': None,
        'wifi bluetooth': None,  
        'weight_kg': None, 
        'warranty_months':None, 
        'price': None,
    }
    catalog['device_type'] = lt.new_list()
    catalog['brand'] = lt.new_list()
    catalog['model'] = lt.new_list()
    catalog['release_year'] = lt.new_list()
    catalog['os'] = lt.new_list()
    catalog['form_factor'] = lt.new_list()
    catalog['cpu_brand'] = lt.new_list()
    catalog['cpu_model'] = lt.new_list()
    catalog['cpu_tier'] = lt.new_list()
    catalog['cpu_cores'] = lt.new_list()
    catalog['cpu_threads'] = lt.new_list()
    catalog['cpu_base_ghz'] = lt.new_list()
    catalog['cpu_boost_ghz'] = lt.new_list()
    catalog['gpu_brand'] = lt.new_list()
    catalog['gpu_model'] = lt.new_list()
    catalog['gpu_tier'] = lt.new_list()
    catalog['vram_gb'] = lt.new_list()
    catalog['ram_gb'] = lt.new_list() 
    catalog['storage_type' ] = lt.new_list() 
    catalog['storage_gb' ] = lt.new_list()
    catalog['storage_drive_count'] = lt.new_list()
    catalog['display_type'] = lt.new_list()
    catalog['display_size_in'] = lt.new_list()
    catalog['resolution'] = lt.new_list()
    catalog['refresh_hz'] = lt.new_list()
    catalog['battery_wh'] = lt.new_list()
    catalog['charger_watts'] = lt.new_list() 
    catalog['psu_watts'] = lt.new_list()
    catalog['wifi'] = lt.new_list()  
    catalog ['bluetooth'] = lt.new_list()  
    catalog['weight_kg'] = lt.new_list() 
    catalog['warranty_months'] = lt.new_list() 
    catalog['price'] = lt.new_list()
    
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    file = data_dir + filename
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    pos = 0
    for cada_computador in input_file:
       
       for llave in cada_computador:
        catalog[llave] = lt.insert_element(catalog[llave], pos, cada_computador[llave])
        pos +=1
    return catalog


#CON SINGLE_LINKED_LIST 
def new_logic_single_linked_list():
    """
    Crea el catalogo para almacenar las estructuras de datos 
    """
    catalog = {
        'device_type': None,
        'brand': None,
        'model': None,
        'release_year': None,
        'os': None,
        'form_factor': None, 
        'cpu_brand': None,
        'cpu_model': None,
        'cpu_tier': None,
        'cpu_cores': None,
        'cpu_threads': None,
        'cpu_base_ghz': None,
        'cpu_boost_ghz': None,
        'gpu_brand': None,
        'gpu_model': None,
        'gpu_tier': None,
        'vram_gb': None,
        'ram_gb': None, 
        'storage_type' : None, 
        'storage_gb' : None, 
        'storage_drive_count': None,
        'display_type' : None,
        'display_size_in': None,
        'resolution' : None,
        'refresh_hz' : None,
        'battery_wh' : None,
        'charger_watts' : None, 
        'psu_watts': None,
        'wifi bluetooth': None,  
        'weight_kg': None, 
        'warranty_months':None, 
        'price': None,
    }
    catalog['device_type'] = sl.new_list()
    catalog['brand'] = sl.new_list()
    catalog['model'] = sl.new_list()
    catalog['release_year'] = sl.new_list()
    catalog['os'] = sl.new_list()
    catalog['form_factor'] = sl.new_list()
    catalog['cpu_brand'] = sl.new_list()
    catalog['cpu_model'] = sl.new_list()
    catalog['cpu_tier'] = sl.new_list()
    catalog['cpu_cores'] = sl.new_list()
    catalog['cpu_threads'] = sl.new_list()
    catalog['cpu_base_ghz'] = sl.new_list()
    catalog['cpu_boost_ghz'] = sl.new_list()
    catalog['gpu_brand'] = sl.new_list()
    catalog['gpu_model'] = sl.new_list()
    catalog['gpu_tier'] = sl.new_list()
    catalog['vram_gb'] = sl.new_list()
    catalog['ram_gb'] = sl.new_list() 
    catalog['storage_type' ] = sl.new_list() 
    catalog['storage_gb' ] = sl.new_list()
    catalog['storage_drive_count'] = sl.new_list()
    catalog['display_type'] = sl.new_list()
    catalog['display_size_in'] = sl.new_list()
    catalog['resolution'] = sl.new_list()
    catalog['refresh_hz'] = sl.new_list()
    catalog['battery_wh'] = sl.new_list()
    catalog['charger_watts'] = sl.new_list() 
    catalog['psu_watts'] = sl.new_list()
    catalog['wifi'] = sl.new_list()  
    catalog ['bluetooth'] = sl.new_list()  
    catalog['weight_kg'] = sl.new_list() 
    catalog['warranty_months'] = sl.new_list() 
    catalog['price'] = sl.new_list()
    
    return catalog

# Funciones para la carga de datos

def load_data_single_linked_list(catalog, filename):
    """
    Carga los datos del reto
    """
    file = data_dir + filename
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    pos = 0
    for cada_computador in input_file:
       
       for llave in cada_computador:
        catalog[llave] = sl.insert_element(catalog[llave], pos, cada_computador[llave])
        pos +=1
    return catalog
# Funciones de consulta sobre el catálogo

#REQUISITO 1 COMPLETADO CON ARRAY_LIST
def req_1(catalog, brand):
    """
    Retorna el resultado del requerimiento 1
    """
    start_time = get_time()
#Crear la lista filtrada de una categoría específica, únicamente con los valores que cumplen con la marca enviada por el usuario.
    def lista_filtrada (categoria): 
        lista = lt.new_list()
        pos = 0
        for posicion in range(0, lt.size(catalog["brand"])):
            if (catalog["brand"]["elements"][posicion] == brand):
                pos = pos + 1
                lista = lt.insert_element(lista, pos, catalog[categoria]["elements"][posicion])
        return lista
  
#Crear la lista por la marca enviada por el usuario y acceder a su tamaño.  
    def solo_marca(categoria):
        marca = lista_filtrada(categoria)
        return lt.size(marca)   
      
 #Encuentra el promedio, mayor y menor de la lista usando funciones de array_list 
    def promedio(lista):
        mayor = float(lt.get_element(lista, 0))
        menor = float(lt.get_element(lista, 0))
        tamaño = lt.size(lista) 
        total = float(lt.get_element(lista, 0))
        pos = 1
        while (pos < lt.size(lista)):
            elemento = lt.get_element(lista, pos)
            total = float(elemento) + total
            if (float(elemento) > mayor):
                mayor = float(elemento)
            elif (float(elemento) < menor):
                menor = float(elemento)
            pos = pos + 1
        promedio = total/ tamaño
        return promedio, menor, mayor  

#Ejecuta el promedio de la lista dado una categoría. 
    def ejecucion(categoria):
        lista = lista_filtrada(categoria)
        return promedio(lista)
    
#Encuentra el computador de menor y mayor precio. 

    
    def model(lista, lista_modelos, lista_peso):
        mayor = float(lt.get_element(lista, 0))
        menor = float(lt.get_element(lista, 0))
        total = float(lt.get_element(lista, 0))
        posicion_mayor = 1
        posicion_menor = 1
        pos = 1
        
        while (pos < lt.size(lista)):
            elemento = lt.get_element(lista, pos)
            total = float(elemento) + total
            if (float(elemento) > mayor):
                mayor = float(elemento)
                posicion_mayor = pos
            elif (float(elemento) == mayor):
                    if (float(lt.get_element(lista_peso, posicion_mayor)) > lt.get_element(lista_peso, pos)):
                        mayor = float(elemento)
                        posicion_mayor = pos
            elif (float(elemento) < menor):
                menor = float(elemento)
                posicion_menor = pos
            elif (float(elemento) == menor):
                    if (float(lt.get_element(lista_peso, posicion_menor)) > lt.get_element(lista_peso, pos)):
                        menor = float(elemento)
                        posicion_menor = pos
            pos = pos + 1
        
        mayor_precio = lt.new_list()
        lt.add_last(mayor_precio, lt.get_element(lista_modelos, posicion_mayor))
        lt.add_last(mayor_precio, mayor)
        
        menor_precio = lt.new_list()
        lt.add_last(menor_precio, lt.get_element(lista_modelos, posicion_menor))
        lt.add_last(menor_precio, menor)
        
        return mayor_precio, menor_precio
            
        
 
#Ejecuta las funciones para hallar el computador de menor y mayor precio.
    def modelo(precio,modelo,peso): 
        lista_precios = lista_filtrada(precio)
        lista_modelos = lista_filtrada(modelo)
        lista_peso = lista_filtrada(peso)
        return model(lista_precios, lista_modelos, lista_peso)
    
    
    end_time = get_time()
    req1_time = delta_time(start_time, end_time)
    
    return solo_marca("brand"), ejecucion("price"), ejecucion("ram_gb"), ejecucion("vram_gb"), ejecucion("cpu_cores"), ejecucion("release_year"), modelo("price", "model", "weight_kg"), req1_time

def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass

def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog, cpu_brand, gpu_model):
    """
    Retorna el resultado del requerimiento 4
    """
    """start_time = get_time()
    
    def lista_filtrada (categoria):
        lista = lt.new_list()
        pos = 0
        for posicion in range(0, lt.size(catalog["cpu_brand"])):
            if (catalog["cpu_brand"]["elements"][posicion] == cpu_brand) and (catalog["gpu_model"]["elements"][posicion] == gpu_model):
                pos = pos + 1
                lista = lt.insert_element(lista, pos, catalog[categoria]["elements"][posicion])
        return lista
    
    def total_computadores (categoria):
        return lt.size(lista_filtrada(categoria))
    
    def promedio(lista):
        lista_original = lista
        lista = lista["elements"]
        total = 0
        for cada_valor in lista:
            total = float(cada_valor) + total
        promedio = total/ lt.size(lista_original) 
        return promedio
    
    def mayor(lista_precios, lista_modelos, lista_peso, lista_cpu, lista_marca, lista_año):
        lista = lista_precios["elements"]
        lista_modelos = lista_modelos["elements"]
        lista_peso = lista_peso["elements"]
        lista_marca = lista_marca["elements"]
        lista_año = lista_año["elements"]
        lista_cpu = lista_cpu["elements"]
        
        mayor = float(lista[0])
        posicion_mayor = 0
        pos = 0
        for cada_valor in lista:
            pos = pos + 1
            if (float(cada_valor) > mayor):
                mayor = float(cada_valor)
                posicion_mayor = pos
            elif (float(cada_valor) == mayor):
                if (lista_peso[posicion_mayor] > lista_peso[pos]):
                    mayor = float(cada_valor)
                    posicion_mayor = pos
        modelo = lista_modelos [posicion_mayor]
        marca = lista_marca[posicion_mayor]
        año = lista_año[posicion_mayor]
        cpu = lista_cpu[posicion_mayor]
        
        return modelo, marca, año, cpu, mayor, posicion_mayor
                    
    def ejecucion(categoria):
        lista = lista_filtrada(categoria)
        promedios = promedio(lista)
        return promedios 
    
    def ejecucion_mayores(precio, modelo, peso, cpu, marca, año):
        lista_precios = lista_filtrada(precio)
        lista_modelos = lista_filtrada(modelo)
        lista_peso = lista_filtrada(peso)
        lista_cpu = lista_filtrada(cpu)
        lista_marca = lista_filtrada(marca)
        lista_año = lista_filtrada(año)
        modelo1, marca1, año1, cpu_model1, precio1, pos = mayor(lista_precios, lista_modelos, lista_peso, lista_cpu, lista_marca, lista_año)
        
        lista_precios = lt.delete_element(lista_filtrada(precio), pos) 
        lista_modelos = lt.delete_element(lista_filtrada(modelo), pos) 
        lista_peso = lt.delete_element(lista_filtrada(peso), pos) 
        lista_cpu = lt.delete_element(lista_filtrada(cpu), pos) 
        lista_marca = lt.delete_element(lista_filtrada(marca), pos) 
        lista_año = lt.delete_element(lista_filtrada(año), pos) 
        modelo2, marca2, año2, cpu_model2, precio2, pos = mayor(lista_precios, lista_modelos, lista_peso, lista_cpu, lista_marca, lista_año)
        
        return modelo1, marca1, año1, cpu_model1, precio1, modelo2, marca2, año2, cpu_model2, precio2
        
        
    
    end_time = get_time()
    req4_time = delta_time(start_time, end_time)

    
    
    return req4_time, total_computadores("cpu_brand"), ejecucion("price"), ejecucion("vram_gb"), ejecucion("ram_gb"), ejecucion("cpu_boost_ghz"), ejecucion_mayores("price", "model", "weight_kg", "cpu_model", "brand", "release_year")"""

    pass

#REQUISITO 5 COMPLETADO CON ARRAY_LIST
def req_5(catalog, filtro, resolucion, año_min, año_max):
    """
    Retorna el resultado del requerimiento 5
    """
    start_time = get_time()
    #Crear la lista filtrada de una categoría específica, únicamente con los valores que cumplen con la resolución y años enviados por el usuario.
    def lista_filtrada (categoria):
        lista = lt.new_list()
        pos = 0
        for posicion in range(0, lt.size(catalog["resolution"])):
            if (catalog["resolution"]["elements"][posicion] == resolucion):
                if (int(catalog["release_year"]["elements"][posicion]) <= int(año_max)) and (int(catalog["release_year"]["elements"][posicion]) >= int(año_min)):
                    pos = pos + 1
                    lista = lt.insert_element(lista, pos, catalog[categoria]["elements"][posicion])
        return lista
    
    #Crear la lista con las condiciones enviadas por el usuario y acceder a su tamaño. 
    def total_computadores (categoria):
        return lt.size(lista_filtrada(categoria))

    #Encuentra el menor precio, y la posición del computador respectivo. 
    def menor(lista_precios):
        menor1 = float(lt.get_element(lista_precios, 0))
        pos = 1
        while (pos < lt.size(lista_precios)):
            elemento = lt.get_element(lista_precios, pos)
            if (float(elemento) < menor1):
                menor1 = float(elemento)
                posicion_menor = pos
            pos = pos + 1
        return  menor1, posicion_menor
    
    #Encuentra el menor precio, y la posición del computador respectivo. 
    def mayor(lista_precios):
        mayor1 = float(lt.get_element(lista_precios, 0))
        pos = 1
        while (pos < lt.size(lista_precios)):
            elemento = lt.get_element(lista_precios, pos)
            if (float(elemento) > mayor1):
                mayor1 = float(elemento)
                posicion_mayor = pos
            pos = pos + 1
        return  mayor1, posicion_mayor
    
    #Encuentra el promedio de una lista usando funciones de array_list.
    def promedio(lista):
        tamaño = lt.size(lista) 
        total = float(lt.get_element(lista, 0))
        pos = 1
        while (pos < lt.size(lista)):
            elemento = lt.get_element(lista, pos)
            total = float(elemento) + total
            pos = pos + 1
        promedio = total/ tamaño
        return promedio

    #Crea las listas filtradas de diferentes categorías
    def listas_filtradas ( tamaño, gpu_tier, display, weight, precio):
        lista_precios = lista_filtrada(precio)
        lista_tamaño = lista_filtrada(tamaño)
        lista_gpu_tier = lista_filtrada(gpu_tier)
        lista_display = lista_filtrada(display)
        lista_weight = lista_filtrada(weight)
        return lista_precios, lista_tamaño, lista_gpu_tier, lista_display, lista_weight

    #Encuentra los datos del computador más barato/más caro
    def computador_filtrado (filtro, tamaño, gpu_tier, display, weight, precio):
        lista_precios, lista_tamaño,lista_gpu_tier,lista_display, lista_weight = listas_filtradas ( tamaño, gpu_tier, display, weight, precio)
        if filtro == "BARATO":
            precio, pos = menor(lista_precios)
        elif filtro == "CARO":
            precio, pos = mayor(lista_precios)
        
        
        tamaño = lt.get_element(lista_tamaño, pos)
        gpu_tier = lt.get_element(lista_gpu_tier, pos)
        display = lt.get_element(lista_display, pos)
        weight = lt.get_element(lista_weight, pos)
        
        return precio, tamaño, gpu_tier, display, weight
    
    #Encuentra el promedio de precio, tamaño, y gpu tier de los computadores que cumplen con el filtro
    def promedio_filtrado( tamaño, gpu_tier, display, weight, precio): 
        lista_precios, lista_tamaño,lista_gpu_tier,lista_display, lista_weight = listas_filtradas ( tamaño, gpu_tier, display, weight, precio)
        
        promedio_precios = promedio(lista_precios)
        promedio_tamaño = promedio(lista_tamaño)
        promedio_gpu_tier = promedio(lista_gpu_tier)
        
        return promedio_precios, promedio_tamaño, promedio_gpu_tier
        
    end_time = get_time()
    req5_time = delta_time(start_time, end_time)
    
    return filtro, req5_time, total_computadores("resolution"), computador_filtrado (filtro, 'display_size_in', "gpu_tier", 'display_type', "weight_kg", "price"), promedio_filtrado('display_size_in', "gpu_tier", 'display_type', "weight_kg", "price")


def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
