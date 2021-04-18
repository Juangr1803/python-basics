# Set------------------
colors = {'RED', 'GREEN', 'BLUE'}

print(type(colors))
print(colors)
# Si Red se encuentra dentro del set
print('RED' in colors)

# Añadir un elemento al set
colors.add('VIOLET')
print(colors)

# Eliminar un elemento al set
colors.remove('VIOLET')
print(colors)

# Limpia todo el set
colors.clear()
print(colors)

# Elimina completamente la variable colors
del colors
print(colors)
