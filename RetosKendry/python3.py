productos = {
   
}

categorias = {
   
}

diccionario = {
   
}

noC = int(input("Introduzca el número de categorías: "))
for noC in range(noC):
    categorias[noC+1] = {
    "nombreC" : input("Introduzca el nombre de la categoría: "),
    "id" : int(input("Introduzca el Id de la categoría: "))
    }
    
    
print(categorias)

noP = int(input("Introduzca el número de productos: "))
for noP in range(noP):
    productos[noP + 1] = {
    "nombre" : input("Introduzca el nombre del producto: "),
    "precio" : int(input("Introduzca el precio del producto: ")),
    "id_categoria" : int(input("Introduzca el Id de la categoría: "))
    }
    
print(productos)

for x in range(len(categorias)):
    for y in range(len(productos)):
        if (categorias[x+1]["id"] == productos[y+1]["id_categoria"]):
            diccionario[y + 1] = {
                "nombre" : productos[y+1]["nombre"],
                "precio" : productos[y+1]["precio"],
                "nombC" : categorias[x+1]["nombreC"]
            }
        
print(diccionario)