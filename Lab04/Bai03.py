def mating_pairs(animals, nums):
  pairs = set()
  num_gerbils = len(animals)
  for i in range(num_gerbils):
    animal = animals.pop()
    num = nums.pop()
    pairs.add((animal, num),)
  return pairs
mating_pairs({'Mouse','Tiger','Dragon'}, {1,3,5})