# def print_message():
#   print('Message special')
#   print('I am learning to use functions')


# print_message()
# print_message()
# print_message()

def conversation(message):
  print('Hello')
  print('How are you?')
  print(message)
  print('bye')

option = int(input("Select a option (1, 2, 3):"))

if option == 1:
  conversation("Select the option first")
if option == 2:
  conversation("Select the option Second")
if option == 3:
  conversation("Select the option Third")
else:
  print("Write the option correct")


def sum(a, b):
  print("Two numbers are added")
  result = a + b
  return result

print(sum(1, 4))