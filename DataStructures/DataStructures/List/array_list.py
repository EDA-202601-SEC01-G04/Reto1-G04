
#PASO 2.2.1 - 3: 
def new_list():
    newlist = {
        'elements': [],
        'size': 0,}
    return newlist

#Paso 2.2.1 - 12:
def get_element(my_list,index):
    
    return my_list ["elements"][index]

def is_present (my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range (0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

#add_first()- V
def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"]+=1
    return my_list

#add_last()- V
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"]+=1
    return my_list

#first_element()- V
def first_element(my_list):
    if my_list["size"] != 0:
        return my_list["elements"][0]
    else: 
        return "IndexError: list index out of range." 

#is_empty()- V
def is_empty(my_list):
    if my_list["size"]==0:
        return True
    else:
        return False

#size()- V
def size(my_list):
    return my_list["size"]

#last_element()- S
def last_element(my_list): 
    return my_list["elements"][-1]


#delete_element()- S
def delete_element(my_list, pos):
    del my_list["elements"][pos] 
    my_list["size"] -= 1
    return my_list

#remove_first()- S
def remove_first(my_list): 
    my_list["size"]-= 1
    element = my_list["elements"][0]
    del my_list["elements"][0] 
    return element

#remove_last()- S
def remove_last(my_list): 
    my_list["size"]-= 1
    element = my_list["elements"][my_list["size"]] 
    del my_list["elements"][my_list["size"]] 
    return element

#insert_element()- M

def insert_element(my_list, pos, element):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list


#change_info()- M

def change_info(my_list, pos, element):
    my_list["elements"][pos] = element
    return my_list


#exchange()- M
def exchange(my_list, pos1, pos2):
    element1 = my_list["elements"][pos1]
    element2 = my_list["elements"][pos2]
    my_list["elements"][pos1] = element2
    my_list["elements"][pos2] = element1
    return my_list


#sub_list()- M

def sub_list(my_list, pos1, pos2):
    newlist = new_list()
    for pos in range(pos1, pos2 + 1):
        insert_element(newlist, newlist["size"], my_list["elements"][pos])
    return newlist

def sub_list(my_list, pos1, pos2):
    newlist = new_list()
    for pos in range(pos1, pos2 + 1):
        insert_element(newlist, newlist["size"], my_list["elements"][pos])
    return newlist
