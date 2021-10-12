def is_balanced(dic):
  balanced=0
  for key, value in dic.items():
    balanced += value
  if balanced == 1:
    return True
  else:
    return False
color = {'R':0.3,'G':0.3,'B':0.2}
is_balanced(color)