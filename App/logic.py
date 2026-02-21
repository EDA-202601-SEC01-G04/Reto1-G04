import time
import csv
import os
csv.field_size_limit(2147483647)
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
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
    # TODO: Realizar la carga de datos

# Funciones de consulta sobre el catálogo


def req_1(catalog, brand):
    """
    Retorna el resultado del requerimiento 1
    """
    marca = lt.new_list()
    pos = 0
    for cada_marca in catalog["brand"]["elements"]:
        if (catalog["brand"]["elements"][cada_marca] == brand):
            pos = pos + 1
            marca = lt.insert_element(marca, pos, catalog["brand"]["elements"][cada_marca])
    return 1
    
    # TODO: Modificar el requerimiento 1
    

def req_2(catalog, precio_max, precio_min):
    """
    Retorna el resultado del requerimiento 2
    """
    t_inicio = time.perf_counter()
    
    size = catalog["price"]["size"]
    #separa las listas de cada categoría
    precios = catalog["price"]["elements"]
    ram = catalog["ram_gb"]["elements"] 
    vram = catalog["vram_gb"]["elements"]
    años = catalog["release_year"]["elements"]
    modelos = catalog["model"]["elements"]
    marcas = catalog["marca"]["elements"]
    cpus = catalog["cpu_brand"]["elements"]
    gpus = catalog["gpu_brand"]["elements"]
    #lleva la cuenta de cuandos PCs cumplen, y sus respectivos valores
    count = 0
    suma_ram = 0
    suma_vram = 0
    suma_precios = 0
    #guarda los resultados que son un diccionario
    moderno = None
    menor_precio = None
    mayor_precio = None
    
    for i in range (size):
        precio = float(precios[i])
        
        if precio_min<=precio<=precio_max:
            count += 1
            suma_ram += float(ram[i])
            suma_vram += float(vram[i])
            suma_precios += precio
            #busco el más moderno
            año = int(años[i])
            if (moderno is None) or (año>moderno["año"]) or ((año==moderno["año"]) and precio>moderno["precio"]):
                moderno = {"modelo": modelos[i], 
                        "marca":marcas[i], 
                        "año":años[i], 
                        "cpu":cpus[i],
                        "gpu":gpus[i],
                        "precio":precio}
            #busco el mas barato        
            if (menor_precio is None) or (precio<menor_precio["precio"]):
                menor_precio = {"modelo": modelos[i], 
                           "marca":marcas[i], 
                           "año":años[i], 
                           "cpu":cpus[i],
                           "gpu":gpus[i],
                           "precio":precio}
            #busco el mas caro
            if (mayor_precio is None) or (precio>mayor_precio["precio"]):
                mayor_precio = {"modelo": modelos[i], 
                           "marca":marcas[i], 
                           "año":años[i], 
                           "cpu":cpus[i],
                           "gpu":gpus[i],
                           "precio":precio}
    #promedios
    if count>0:
        promedio_ram = suma_ram/count
        promedio_vram = suma_vram/count
        promedio_precios = suma_precios/count
    else: 
        promedio_ram = 0
        promedio_precios = 0
        promedio_vram = 0
    
    t_fin = time.perf_counter()
    tiempo_ejecucion = (t_fin - t_inicio)*1000
    
    return {"tiempo_ejecucion_ms":tiempo_ejecucion,
            "cantidad_computadores":count,
            "promedio_ram":promedio_ram,
            "promedio_vram":promedio_vram,
            "promedio_precios":promedio_precios,
            "computador_mas_moderno": moderno,
            "computador_menor_precio":menor_precio,
            "computador_mayor_precio":mayor_precio}


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

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
