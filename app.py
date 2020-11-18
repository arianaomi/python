
# FILE

# crear un archivo (nombre, permisos)
"""
    Permisos:
        w+ -> escribir, sobreescibir
        a+ -> empieza a escribir al fianl del archivo
"""
f = open ('my_file.txt','a+')
f.write('escribo de nuevo al final')
f.close ()

# Leer un archivo

file = open ('my_file.txt','r')
content = file.read()
print(content)