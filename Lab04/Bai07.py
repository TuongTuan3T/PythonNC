def count_duplicates(dict):
  fun = []
  for key, value in dict.items():
    if value in fun:
      print(value)
    else:
      fun.append(value)
dict = {1,9,7,2,5,7,6}
count_duplicates(dict)