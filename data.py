

name1 = " "
surname1 = " "
telefon1 = " "
description1 = " "

def id (x1,x2,x3,x4):
    global name1
    global surname1
    global telefon1
    global description1
    name1 = x1
    surname1 = x2
    telefon1 = x3
    description1 = x4

def get_id():
    global name1
    global surname1
    global telefon1
    global description1
    return(name1,surname1,telefon1,description1)


