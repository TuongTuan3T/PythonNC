class Country:
  def __init__(self, name: str, population: int, area:float):
    self.name = name
    self.population = population
    self.area = area
  def is_larger(self, other):
    if (self.area > other.area):
      return True
    else:
      return False
  def population_destiny(self):
    return self.population/self.area
  def _str_ (self):
    return ('{} has a population of {} and is {} sqare km'.format(self.name, self.population, self.area))
  def __repr__(self):
    return ("Country('{0}', {1}, {2})".format(self.name, self.population, self.area))
usa = Country('United States of America', 313914040, 9826675)
canada = Country("Cananda", 34482779, 9984670)
mexico = Country('Mexico', 112336538, 1943950)

#Câu a
print(canada.name)
print(canada.population)
print(canada.area)

#Câu b
print(canada.is_larger(usa))
print(usa.is_larger(canada))

#Câu c
print(canada.population_destiny())

#Câu d
usa = Country('United States of America', 313914040, 9826675)
print(usa)

#Câu e
canada = Country('Canada', 34482779, 9984670)
print(canada)
print([canada])