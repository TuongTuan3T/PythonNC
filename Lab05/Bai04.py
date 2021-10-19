class Nematode:
  def __init__(self, lenght:int, gender:str, age: int):
    self.lenght = lenght
    self.gender = gender
    self.age = age
  def __str__(self):
    return ('Celegan is : \n+ lenght {}mm \n+ gender is {} \n+ age = {} days '.format(self.lenght, self.gender, self.age))
  def __repr__(self):
    return ('{} {} {}'.format(self.lenght, self.gender, self.age))
Celegan = Nematode(1, 'male', 9)
print(Celegan.__str__())
print(Celegan.__repr__())