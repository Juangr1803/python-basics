# Variable de Texto-----------
message="""This is a message
with tree jumps
of line"""

# Variables numericas-----------
number1 = 5
number2 = 7

# Condicional if--------------
if number1 > number2:
  print("The number one is mayor")
else:
  print("The number two is menor")

# Funciones
def msg():
  print("The number two is menor")
  print("The number two is menor")

msg()

# Funciones con parametros-----------
def suma(num1,num2):
  res = num1 + num2
  print(res)
  return res

suma(2,5)
suma(4,7)
suma(9,1)
print(suma(2,3))

add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(1,2))



# Listas (Arreglos)-----------
myList = ['Juan', 'Valentina']
myList = ['Juan', 'Valentina'] * 3
myList2 = ['Juan', 3, True, 57.79, 'Valentina']

# Unir listas
myList3 = myList + myList2
# agregar un elemento en una lista
myList.append("Hanna") 
# insertar un elemento en una lista
myList.insert(2,"Sandra")
# concatenar elementos en una lista
myList.extend(["Maria","Edgar"])
# elimina elementos en una lista
myList2.remove("Valentina")
myList2.remove(3)
# elimina el ultimo elemento de la lista
myList2.pop()
# mostrar en que indice se encuentra el elemento (posicion)
print(myList.index("Juan"))
# imprime true/false si se encuentra el elemento en la lista
print("Valentina" in myList)

print(myList[:])
print(myList2[:])
print(myList3[:])
print(myList2[0])


# Tuplas------------------
myTupla = ("Juan", 18, 1, 2003)

# Comvertir una tupla a una lista
myListToTupla = list(myTupla)
# Comvertir una lista a una tupla
myTuplaToList = tuple(myList)

print(myTupla[2])
print(myListToTupla[:])
print(myTuplaToList[:])



