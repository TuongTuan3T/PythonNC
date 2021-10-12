def dict_intersect(dic1,dic2):
  dic3 = {}
  for key, value in dic1.items():
    for key1, value1 in dic2.items():
      if ((key == key1) and (value ==value1)):
        dic3[key] = value
  return dic3
dic1 = {'red': 1, 'green': 1, 'blue': 2}
dic2 = {'red': 1, 'green': 5, 'blue': 2, 'black': 4}
dict_intersect(dic1,dic2)