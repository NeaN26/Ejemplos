# Estructuras de datos por listas

cursos = ["Python", "django", "flask", "c", "c++", "c#", "java", "php"]

print("Mostrar el primer elemento de la lista")
curso = cursos[0]
print(curso)

print("Mostrar el último elemento de la lista")
curso = cursos[-1]
print(curso)

print('Mostrar Sub-Listas')
print("Mostrar los elementos desde el index 3 hasta el index 7")
sub = cursos[3:7]
print(sub)

print("Mostrar los elementos desde el index 0 hasta el index 7")
sub = cursos[:7]
print(sub)

print("Mostrar los elementos desde el index 5 hasta el último index ")
sub = cursos[5:]
print(sub)

print("Mostrar los elementos de la lista sin modificar")
sub = cursos[:]
print(sub)

print("Mostrar los elementos desde el index 1 hasta el index 7 con saltos de 2 en 2")
sub = cursos[1:7:2]
print(sub)

print("Mostrar los elementos inversa")
sub = cursos[::-1]
print(sub)

"""Estas son las formas en las cuales podemos crear una nueva lista (sublistas) a partir de otra.

    [:] Todos los elementos.
    [start:] Todos los elementos desde el índice establecido(start).
    [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
    [start:end] Todos los elementos de un rango de índices.
    [start:end:step] Todos los elementos de un rango de índices con saltos.

    De igual forma, este listado es aplicable a las tuplas y los strings."""
