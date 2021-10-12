
def count_values(dic):
  fun = []
  for key, value in dic.items():
    fun.append(value)
  for key, value in dic.items():
    count = 0
    for i in fun:
      if i == value:
        count = count + 1
    if count == 1:
      print(value)
dic = {'red': 1, 'green': 1, 'blue': 2}
count_values(dic)