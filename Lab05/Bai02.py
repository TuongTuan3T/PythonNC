class Continent(Country):
    def __init__(self,name, countries):
      self.name = name
      self.countries = countries
    def total_population(self):
      total = 0
      for country in north_america.countries:
        total += country.population
      return total
    def america(self):
      num = 0
      for country in north_america.countries:
        num+=1
        print(country)
      return ''
mexico = Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)
##Câu a
print(mexico)
print(north_america.name)
print('--------------------------------')
##Câu b
print('The total population of the three countries is :')
print(north_america.total_population())
print('--------------------------------')
##Câu c
print(north_america.america())