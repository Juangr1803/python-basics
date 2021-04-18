# Conditional -----------
x = 40
y = 20


if x > y:
  print('X es mayor que Y')
else:
  print('X es menor que Y')


if x < y:
  print('X es menor que Y')
elif x > y:
  print('X es mayor que Y')
else:
  print('X y Y son iguales')


if x < 50 and x > y:
  print('X es menor que 50 y mayor que Y')
if x < 50 or x > y:
  print('X es menor que 50 o mayor que Y')
if (not(x == y)):
  print('X y Y son diferentes')

