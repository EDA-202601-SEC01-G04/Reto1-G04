
from . import list_node as ln

#PASO 2.2.1 - 4: 
def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,}
    return newlist

#PASO 2.2.1 - 13:
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node ["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function (element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count = -1
    return count

#add_first()- S
def add_first(my_list, element):
    node = ln.new_single_node(element)
    if my_list["first"] is not None:
        node ["next"] = my_list["first"]
    my_list["first"] = node
    if my_list["size"] == 0:
        my_list["last"] = node
    my_list["size"]+= 1
    return my_list

#add_last()- S
def add_last(my_list, element): 
    node = ln.new_single_node(element)
    if my_list["last"] is not None:
        my_list["last"]["next"] = node
    my_list["last"] = node
    if my_list["size"] == 0:
        my_list["first"] = node
    my_list["size"]+= 1
    return my_list

#size()- S
def size(my_list): 
    return my_list["size"]

#first_element()- M
def first_element(my_list):
   return my_list["first"]["info"]




#is_empty()- S
def is_empty(my_list): 
    return my_list["size"] == 0


#last_element()- S
def last_element(my_list): 
    return my_list["last"]["info"]

#delete_element()- M
def delete_element(my_list, pos):
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
    else:
        searchpos = 0
        node = my_list["first"]
        while searchpos < pos - 1:
            node = node ["next"]
            searchpos += 1
        node ["next"] = node ["next"]["next"]
    my_list["size"] -= 1
    return my_list


#remove_first()- M

def remove_first(my_list):
    element = my_list["first"]["info"]
    node = my_list["first"]
    my_list["first"]= node["next"]
    my_list["size"] -= 1
    return element
    


#remove_last()- M
def remove_last(my_list):
    element = my_list["last"]["info"]
    searchpos = 0
    node = my_list["first"]
    while searchpos < (my_list["size"]-1):
        node = node ["next"]
        searchpos += 1
    node["next"] = None
    my_list["last"]= node
    return element
    

#insert_element()- M

def insert_element(my_list, element, pos):
    node = ln.new_single_node(element)
    if pos == 0:
        node ["next"] = my_list["first"]
        my_list["first"] = node
        if my_list["size"] == 0:
            my_list["last"] = node
    else:
        searchpos = 0
        current_node = my_list["first"]
        while searchpos < (pos - 1):
            current_node = current_node ["next"]
            searchpos += 1
        current_node ["next"] = node
        node ["next"] = current_node ["next"]["next"]
        if node ["next"] is None:
            my_list["last"] = node
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos<0 or pos>=my_list["size"]:
        return "IndexError: list index out of range."
    else:
        this_node = my_list["first"]
        this_pos = 0
        
        while this_pos<pos:
            this_node = this_node["next"]
            this_pos += 1
        
        this_node["info"]=new_info
    return my_list
           
def exchange(my_list, pos_1, pos_2):
    if (pos_1<0 or pos_1 >= my_list["size"]) or (pos_2<0 or pos_2 >= my_list["size"]):
        return ("IndexError: list index out of range.")
    elif pos_2 == pos_1:
        return my_list
    else:
        this_node1 = my_list["first"]
        this_pos1 = 0
        while this_pos1<pos_1:
            this_node1 = this_node1["next"]
            this_pos1 += 1
        node1 = this_node1
        
        this_node2 = my_list["first"]
        this_pos2 = 0
        while this_pos2<pos_2:
            this_node2 = this_node2["next"]
            this_pos2 += 1
        node2 = this_node2
        
        x = node1["info"]
        node1["info"] = node2["info"]
        node2["info"] = x
    
    return my_list

def sub_list(my_list, pos, num_elements):
    if pos<0 or pos>=my_list["size"]:
        return "IndexError: list index out of range."
    else:
        resp_list = new_list()
        this_node = my_list["first"]
        this_pos = 0
        while this_pos < pos:
            this_node = this_node["next"]
            this_pos += 1
        
        count = 0
        while (count < num_elements) and (this_node != None):
            add_last(resp_list, this_node["info"])
            this_node = this_node["next"]
            count += 1
            
        return resp_list
    
