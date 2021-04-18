def run():
  LIMIT = 1000

  count = 0
  potentia_2 = 2 ** count
  while potentia_2 < LIMIT:
    print(potentia_2)
    count += 1
    potentia_2 = 2 ** count


if __name__ == "__main__":
  run()