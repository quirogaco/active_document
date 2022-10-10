

def unique(text):
    print("set:", set(text))
    lista = list(set(text))

    return lista[0]

text = "hajfjgñlsfhf"

print( unique(text) )