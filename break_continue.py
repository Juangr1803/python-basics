def run():
  # for count in range(1000):
  #   if count % 2 != 0:
  #     continue
  #   print(count)

  for i in range(10000):
    print(i)
    if i == 5678:
      break

  text = input("Write a text: ")
  for lettter in text:
    if lettter == 'o':
      break
    print(lettter)

if __name__ == '__main__':
  run()