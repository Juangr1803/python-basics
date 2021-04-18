def converter(type_pesos, value_dollar):
  pesos = input("How many " + type_pesos + " pesos do you have?:")
  pesos = float(pesos)
  value_dollar = value_dollar
  dollars = pesos / value_dollar
  dollars = round(dollars, 2)
  dollars = str(dollars)
  print('Do you have $' + dollars + ' dollars')

menu = """
Welcome to converter of coins 😁 !!

1 - Colombian Pesos
2 - Argentine Pesos
3 - Mexican Pesos

Select a option: """

option = int(input(menu))

if option == 1:
  converter("Colombian",3875)
elif option == 2:
  converter("Argentine",65)
elif option == 3:
  converter("Mexican",24)
else:
  print('Insert a option sucess, please')


# Pesos to Dollars

# pesos = input("How many Colombian pesos do you have?:")
# pesos = float(pesos)
# value_dollar = 3875
# dollars = pesos / value_dollar
# dollars = round(dollars, 2)
# dollars = str(dollars)
# print('Do you have $' + dollars + ' dollars')

# Dollars to Pesos

# dollars = input("How many USA dollars do you have?:")
# dollars = float(dollars)
# value_pesos = 3875
# pesos = dollars * value_pesos
# pesos = round(pesos,2)
# pesos = str(pesos)
# print('Do you have $' + pesos + ' pesos')