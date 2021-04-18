def run():
  my_dictionary = {
    'key1': 1,
    'key2': 2,
    'key3': 3,
  }
  print(my_dictionary['key1'])
  print(my_dictionary['key2'])
  print(my_dictionary['key3'])

  people_countries = {
    'Argentine': 44938712,
    'Brasil': 210147125,
    'Colombian': 50372424,
  }

  # print(people_countries['Bolivia']) Error

  # for country in people_countries.keys():
  #   print(country)

  for country, people in people_countries.items():
    print(country, ' : ', people)

if __name__ == '__main__':
  run()