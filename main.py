from random import randint
from sklearn.linear_model import LinearRegression

def generate_training_set() -> list:
  training_data = []
  for _ in range(100):
    item = [randint(0, 1000) for _ in range(3)]
    data.append(item)
  return training_data

def generate_training_outputs(x1, x2, x3) -> list:
  training_outputs = []
  for _ in range(100):
    equation = x1 + 2*x2 + 3*x3
    training_outputs.append(equation)
  return training_outputs

def predict(predictor, test_set: list):
  outcome = predictor.predict(X=test_set)
  coefficients = predictor.coef_
  print("Prediction:", outcome)
  print("Coefficients", coefficients)


def main():
  train_inputs = generate_training_set()
  x1 = 0
  x2 = 0
  x3 = 0
  for items in train_inputs:
    for i in items:
      if i == 0:
        x1 = items[i]
      elif i == 1:
        x2 = items[i]
      else:
        x3 = items[i]
      

  train_outputs = generate_training_outputs(x1, x2, x3)
  predictor = LinearRegression(n_jobs=-1)
  predictor.fit(X=train_input, y=train_outputs)
  X_test = [[10, 20, 30]]
  predict(predictor, X_test)

if __name__ == "__main__":
  main()


