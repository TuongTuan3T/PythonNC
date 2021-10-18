class Student:
  def __init__(self, name:str, number: str, course:str, mail:str):
    self.name = name
    self.number = number
    self.course = course
    self.mail = mail
  def __str__(self):
    return ('{}\n{}\n{}\n{} '.format(self.name, self.number, self.course, self.mail))
pupil = Student('TuongTuan', '187it07012', 'tuongtuan@yahoo.com', 'K10' )
##Câu a
print(pupil)