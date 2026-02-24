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
        'wifi': None,  
        'bluetooth': None,  
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
        sl.add_last (catalog[llave], cada_computador[llave])
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

#REQUISITO 4 COMPLETADO CON SINGLE_LINKED_LIST
def req_4(catalog, cpu_brand, gpu_model):
    """
    Retorna el resultado del requerimiento 4
    """
    start_time = get_time()
    
     #Crear la lista filtrada de una categoría específica, únicamente con los valores que cumplen con la resolución y años enviados por el usuario.
    def lista_filtrada (categoria):
        lista = sl.new_list()
        for posicion in range(0, sl.size(catalog["cpu_brand"])):
            if (sl.get_element(catalog["cpu_brand"], posicion) == cpu_brand) and (sl.get_element(catalog["gpu_model"], posicion) == gpu_model):
                sl.add_last(lista, sl.get_element(catalog[categoria], posicion))
        return lista
 
    #Encontrar promedio de la lista con funciones de single_linked_list.
    def promedio(lista):
        curr = lista["first"]
        total = float(curr["info"])
        for i in range(0, sl.size(lista) - 1):
            curr = curr["next"]
            total = total + float(curr["info"])
            
        promedio = total/sl.size(lista)
        return promedio
    
    #Crear todas las listas filtradas para hallar el promedio.
    def listas_filtradas_promedio(precio, vram, ram, cpu_boost):
        lista_precios = lista_filtrada(precio)
        lista_vram = lista_filtrada(vram)
        lista_ram = lista_filtrada(ram)
        lista_cpu_boost = lista_filtrada(cpu_boost)
        return lista_precios, lista_vram, lista_ram, lista_cpu_boost
    
    #Crear todas las listas filtradas para hallar el info de los computadores más costosos.
    def listas_filtradas_mayor(model, marca, año, cpu_model, precio, peso):
        lista_modelo = lista_filtrada(model)
        lista_marca = lista_filtrada(marca)
        lista_año = lista_filtrada(año)
        lista_cpu_model = lista_filtrada(cpu_model)
        lista_precio = lista_filtrada(precio)
        lista_peso = lista_filtrada(peso)
        return lista_modelo, lista_marca, lista_año, lista_cpu_model, lista_precio, lista_peso
    
    #Encontrar el promedio de 5 categorías.
    def promedios_5 (precio, vram, ram, cpu_boost):
        lista_precios, lista_vram, lista_ram, lista_cpu_boost = listas_filtradas_promedio(precio, vram, ram, cpu_boost) 
        tamaño_computadores = sl.size(lista_precios)
        promedio_precios = promedio(lista_precios)
        promedio_vram = promedio(lista_vram)
        promedio_ram = promedio(lista_ram)
        promedio_cpu_boost = promedio(lista_cpu_boost)
        return tamaño_computadores, promedio_precios, promedio_vram, promedio_ram, promedio_cpu_boost
   
    #Encontrar el computador más costoso.
    def computador_mas_costoso (lista, lista_peso):
        curr = lista["first"]
        mayor = curr
        posicion_mayor = 0
        for i in range(1, sl.size(lista)):
            curr = curr["next"]
            if float(curr["info"]) > float((mayor["info"])):
                mayor = curr
                posicion_mayor = i
            elif float(curr["info"]) == float((mayor["info"])):
                if float(sl.get_element(lista_peso, i)) < float(sl.get_element(lista_peso, posicion_mayor)):
                    mayor = curr
                    posicion_mayor = i
        return mayor, posicion_mayor
    
    #Encontrar los dos computadores más costosos.
    def dos_mayores (lista, lista_peso): 
        mayor_1, posicion_mayor_1 = computador_mas_costoso (lista, lista_peso)
        lista = sl.delete_element(lista, posicion_mayor_1)
        mayor_2, posicion_mayor_2 = computador_mas_costoso (lista, lista_peso)
        if (posicion_mayor_2 >= posicion_mayor_1):
            posicion_mayor_2 = posicion_mayor_2 + 1
        mayor_1 = mayor_1["info"]
        mayor_2 = mayor_2["info"]
        return mayor_1, posicion_mayor_1, mayor_2, posicion_mayor_2 
    
    #Encontrar la info demlos dos computadores más costosos.
    def info_mas_costosos (model, marca, año, cpu_model, precio, peso):
            lista_modelo, lista_marca, lista_año, lista_cpu_model, lista_precio, lista_peso = listas_filtradas_mayor(model, marca, año, cpu_model, precio, peso)
            mayor_1, posicion_mayor_1, mayor_2, posicion_mayor_2 = dos_mayores (lista_precio, lista_peso)
            modelo1 = sl.get_element(lista_modelo, posicion_mayor_1)
            modelo2 = sl.get_element(lista_modelo, posicion_mayor_2)
            marca1 = sl.get_element(lista_marca, posicion_mayor_1)
            marca2= sl.get_element(lista_marca, posicion_mayor_2)
            año1 = sl.get_element(lista_año, posicion_mayor_1)
            año2 = sl.get_element(lista_año, posicion_mayor_2)
            cpu_model1 = sl.get_element(lista_cpu_model, posicion_mayor_1)
            cpu_model2 = sl.get_element(lista_cpu_model, posicion_mayor_2)
            return mayor_1, mayor_2, modelo1, modelo2, marca1, marca2, año1, año2, cpu_model1, cpu_model2
    
    
    end_time = get_time()
    req4_time = delta_time(start_time, end_time)
    return req4_time, promedios_5("price", "vram_gb", "ram_gb", "cpu_boost_ghz"), info_mas_costosos ("model", "brand", "release_year", "cpu_model", "price", "weight_kg")

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
