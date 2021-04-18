myStr = 'Hello World'

print(myStr.upper()) #  String en Mayusculas
print(myStr.lower()) # String en Minusculas
print(myStr.swapcase()) # String en minusculas a mayusculas
print(myStr.capitalize()) # Primera palabra en Mayuscula
print(myStr.replace('Hello', 'bye')) # Remplaza un string por otro diferente
print(myStr.count('o')) # Cuenta cuantas veces se repite el string

print(myStr.startswith('Hello')) # Si el string empieza con la palabra Hello
print(myStr.endswith('World')) # Si el string termina con la palabra world

print(myStr.split()) # Divide la cadena de string 
print(myStr.split('o')) # Divide el string a partir de la letra o
print(myStr.find('o')) # Devuelve la posicion del string en donde se encuentra la letra o
print(myStr.find(' ')) # Devuelve la posicion del string en donde se encuentra un espacio

print(len(myStr)) # Devuelve cuantos indices 'longitud' del string
print(myStr.index('e')) # Devuelve el indice de la letra e

print(myStr.isnumeric()) # Si es numerico
print(myStr.isalpha()) # Si es alpha numerico

print(myStr[4]) # Devuelve el string de la posicion en la que se encuentra el indice
print(myStr[-1]) # Devuelve el string en la posicion inversa en la que se encuentra el indice

