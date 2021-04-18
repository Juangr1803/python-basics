def is_primo(number):
  # count = 0
  # for i in range(1,number + 1):
  #   if i == 1 or i == number:
  #     continue
  #   if number % i == 0:
  #     count += 1
  # if count == 0:
  #   return True
  # else:
  #   return False

  for i in range(1, number + 1):
    if i == 1 or i == number:
      continue
    if number % i == 0:
      print(i)
      return False
    else:
      return True

def run():
  number = int(input('Write a number: '))
  if is_primo(number):
    print("Is primo")
  else:
    print("Not is primo")


if __name__ == '__main__':
  run()