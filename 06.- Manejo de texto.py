texto = "curso de Python 3"

# Prímera letra Mayúscula.
resultado = texto.capitalize()
print(resultado)

# Cambiar minúsculas por mayùsculas.
resultado2 = texto.swapcase()
print(resultado2)

# Cambiar todo a mayúscula
resultado3 = texto.upper()
print(resultado3)

# Cambiar todo a minúscula
resultado4 = texto.lower()
print(resultado4)

print(resultado4.isupper())
print(resultado4.islower())

# Crear formato de título.
resultado5 = texto.title()
print(resultado5)

# Reemplazar una palabra
resultado6 = texto.replace("Python", "Skate")
print(resultado6)
resultado6 = resultado6.title()
print(resultado6)

texto2 = "      Curso Python bàsico          "
resultado7 = texto2.strip()
print(resultado7)