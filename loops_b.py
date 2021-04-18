# Loops ----------

foods = ['apples','bread','cheese', 'milk', 'bananas']

for food in foods:
  if food == "cheese":
    print('You have to buy this')
  elif food == "milk":
    break
  elif food == "apples":
    continue
  print(food)

for letter in "Hello":
  print(letter)

# Loop while
count = 4

while count < 10:
  count += 1
  print(count)