import random

def password_generator():
  capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','N','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  simbols = ['!', '#', '$', '&', '/', '(', ')', '@', '*', '`', '~']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  characters = capital_letters + lowercase + simbols + numbers

  password = []

  for i in range(20):
    characters_random = random.choice(characters)
    password.append(characters_random)

  password = ''.join(password)
  print(password)

def run():
  password = password_generator()
  print('Your new password is: {}'.format(password))

if __name__ == '__main__':
  run()