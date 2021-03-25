from random import randint
import scikit_learn

def generate_training_set() -> []:
  data = []
  for _ in range(100):
    item = [randint(0, 1000) for _ in range(3)]
    data.append(item)
  return data
