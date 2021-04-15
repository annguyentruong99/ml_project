from random import randint
from sklearn.linear_model import LinearRegression

def generate_training_set() -> list:
  training_data = []
  for _ in range(100):
    item = [randint(0, 1000) for _ in range(3)]
    training_data.append(item)
  return training_data

def generate_training_outputs(arr: list) -> list:
  training_outputs = []
  for list in arr:
    result = list[0] + 2*list[1] + 3*list[2]
    training_outputs.append(result)
  return training_outputs

def predict(predictor, test_set: list):
  outcome = predictor.predict(X=test_set)
  coefficients = predictor.coef_
  print("Prediction:", outcome)
  print("Coefficients", coefficients)


def main():
  train_inputs = generate_training_set()
  train_outputs = generate_training_outputs(train_inputs)
  predictor = LinearRegression(n_jobs=-1)
  predictor.fit(X=train_inputs, y=train_outputs)
  X_test = [[10, 20, 30]]
  predict(predictor, X_test)

if __name__ == "__main__":
  main()


