import random

def run():
  number_random = random.randint(1,100)
  number_select = int(input('Chooise a number from 1 to 100: '))
  while number_select != number_random:
    if number_select < number_random:
      print("Search a number more big")
      number_select = int(input("Chooise other number: "))
    else:
      print('Search a number more small')
      number_select = int(input("Chooise other number: "))
  print('Win !')


if __name__ == '__main__':
  run()


my_tupla = (1, 2, 3, 4, 5)

my_tupla.count(3)
my_tupla.index(2)


# from random import randrange


# def run():
#   random_number = randrange(1,101)
#   start_game = True

#   while start_game:
#     entry_number = int(input('Write a number from 1 to 101: '))
#     if entry_number == random_number:
#       print("Great your win!")
#       start_game = False
#     elif entry_number < random_number:
#       print("The number is big!")
#     else:
#       print("The number is minor!")

# if __name__ == '__main__':
#   run()