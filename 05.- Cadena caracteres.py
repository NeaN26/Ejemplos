lenguajes = "Python; Java; Ruby; Swift; JavaScript; C#; C; C++"

#Separar cadena por espacio
resultado = lenguajes.split()
print(resultado)

# separar por ;
resultado2 = lenguajes.split(";")
print(resultado2)

# sin ; ni espacios
separador = "; "
resultado3 = lenguajes.split(separador)
print(resultado3)

# Unir con espacios
nuevo_string = " ".join(resultado3)
print(nuevo_string)

# Unir con ;
nuevo_string2 = separador.join(resultado3)
print(nuevo_string2)

texto = """ Hola! Hola!
Cómo estás?
chao
chao

felicidad.
"""

# Crea lista con saltos de lìneas.
resultado4 = texto.splitlines()
print(resultado4)