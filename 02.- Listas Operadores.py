lista = [8.17, 90, 1, 5, 44, 1.32]
print(lista)

# Ordena de menor a mayor.
lista.sort()
print(lista)

# Ordena de mayor a menor.
lista.sort(reverse=True)
print(lista)

# lista ya ordena, muestro el valor 1.
mayor = lista[0]
print(mayor)

# lista de menor a mayor en posición 1.
menor = min(lista)
print(menor)

# función mayor.
may = max(lista)
print(may)

# contar los elementos de la lista.
longitud = len(lista)
print(longitud)

# buscar un valor en una lista, resultado booleano.
resultado = 8 in lista
print(resultado)

resultado2 = 8.17 in lista
print(resultado2)

lista = [8.17, 90, 1, 5, 44, 1.32]

# buscar el indice del elemento en la lista con mètodo index.
indice = lista.index(90)
print(indice)

# contar la cantidad de veces que un elento se encuentra en la lista.
# si no se encuentra en la lista, devuelve 0.
contador = lista.count(90)
print(contador)
