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
    inicio = get_time()
    
    total = lt.size(catalog["price"])
    
    resp = sl.new_list()
    
    for i in range(total):
        precio = float(lt.get_element(catalog["price"], i))
        
        if precio_min <= precio <= precio_max:
            computador = {"model": lt.get_element(catalog["model"], i),
                "brand": lt.get_element(catalog["brand"], i),
                "release_year": int(lt.get_element(catalog["release_year"], i)),
                "cpu_brand": lt.get_element(catalog["cpu_brand"], i),
                "gpu_brand": lt.get_element(catalog["gpu_brand"], i),
                "ram_gb": float(lt.get_element(catalog["ram_gb"], i)),
                "vram_gb": float(lt.get_element(catalog["vram_gb"], i)),
                "price": precio,
                "weight_kg": float(lt.get_element(catalog["weight_kg"], i))}
            sl.add_last(resp, computador)
        
    cantidad_resultados = sl.size(resp)
        
    if cantidad_resultados == 0:
        return None
        
    suma_precios = 0
    suma_vram = 0
    suma_ram = 0
    moderno = None
    menor_precio = None
    mayor_precio = None
        
    nodo = resp["first"]
    while nodo is not None:
        x = nodo["info"]
        suma_vram += x["vram_gb"]
        suma_ram += x["ram_gb"]
        suma_precios += x["price"]
        
        if moderno is None: 
            moderno = x
        elif x["release_year"] > moderno["release_year"]:
            moderno = x
        elif (x["release_year"] == moderno["release_year"]) and (x["price"] > moderno["price"]):
            moderno = x
            
        if menor_precio is None:
            menor_precio = x
        elif x["price"] < menor_precio["price"]:
            menor_precio = x
            
        if mayor_precio is None:
            mayor_precio = x
        elif x["price"] > mayor_precio["price"]:
            mayor_precio = x
            
        nodo = nodo["next"]
    
    fin = get_time()
    tiempo = delta_time(inicio, fin) * 1000
    
    return {"tiempo_ms": tiempo,
            "cantidad": cantidad_resultados,
            "promedio_ram": suma_ram/cantidad_resultados,
            "promedio_vram": suma_vram/cantidad_resultados,
            "promedio_precios": suma_precios/cantidad_resultados,
            "mas_moderno": moderno,
            "menor_precio": menor_precio,
            "mayor_precio": mayor_precio}

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

def req_6(catalog, año_inicial, año_final):
    """
    Retorna el resultado del requerimiento 6
    """
    inicio  = get_time()
    
    total = lt.size(catalog["price"])
    
    dicc_sist_op = {}
    cantidad_resultados = 0
    
    for i in range (total):
        año = int(lt.get_element(catalog["release_year"], i))
        
        if año_inicial <= año <= año_final:
            sist_op = lt.get_element(catalog["os"], i)
            computador = {"model": lt.get_element(catalog["model"], i),
                "brand": lt.get_element(catalog["brand"], i),
                "release_year": año,
                "cpu_model": lt.get_element(catalog["cpu_model"], i),
                "gpu_model": lt.get_element(catalog["gpu_model"], i),
                "price": float(lt.get_element(catalog["price"], i)),
                "weight_kg": float(lt.get_element(catalog["weight_kg"], i))}
            
            if sist_op not in dicc_sist_op:
                dicc_sist_op[sist_op] = lt.new_list()
            lt.add_last(dicc_sist_op[sist_op], computador)
            cantidad_resultados += 1
            
    if cantidad_resultados == 0:
        return None      
      
    resumen_sist_op = {}
    sist_op_mas_usado = None
    sist_op_mayor_recaudo = None
    
    for sist_op, lista in dicc_sist_op.items():
        n = lt.size(lista)
        suma_precio = 0
        suma_peso = 0
        mas_costoso = None
        mas_barato = None
        
        for j in range (n):
            x = lt.get_element(lista, j)
            suma_precio += x["price"]
            suma_peso += x["weight_kg"]
            
            if (mas_costoso is None) or (x["price"]>mas_costoso["price"]):
                mas_costoso = x
            if (mas_barato is None) or (x["price"]<mas_barato["price"]):
                mas_barato = x
        
        recaudo = suma_precio
        resumen_sist_op[sist_op] = {"total": n,
                                    "recaudo": recaudo,
                                    "promedio_precio": suma_precio / n,
                                    "promedio_peso": suma_peso / n,
                                    "mas_costoso": mas_costoso,
                                    "mas_barato": mas_barato}
        
        if (sist_op_mas_usado is None) or (n>resumen_sist_op[sist_op_mas_usado]["total"]):
            sist_op_mas_usado = sist_op
        if (sist_op_mayor_recaudo is None) or (recaudo>resumen_sist_op[sist_op_mayor_recaudo]["recaudo"]):
            sist_op_mayor_recaudo = sist_op
            
    fin = get_time()
    tiempo = delta_time(inicio, fin) * 1000
    
    return {"tiempo_ms": tiempo,
            "cantidad": cantidad_resultados,
            "sist_op_mas_usado": {"nombre":sist_op_mas_usado, 
                                  "total":resumen_sist_op[sist_op_mas_usado]["total"], 
                                  "recaudo": resumen_sist_op[sist_op_mas_usado]["recaudo"]},
            "sist_op_mayor_recaudo": {"nombre":sist_op_mayor_recaudo, 
                                  "total":resumen_sist_op[sist_op_mayor_recaudo]["total"], 
                                  "recaudo": resumen_sist_op[sist_op_mayor_recaudo]["recaudo"]},
            "resumen_sist_op": resumen_sist_op}  
    


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
