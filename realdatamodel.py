import csv
from sklearn.linear_model import LinearRegression

def generate_training_inputs(file_name: str) -> list:
  """
  Function to generate the training inputs
  :param: file_name: str
  :return: training_inputs: list
  """
  training_inputs = []
  with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    if header != None:
      for row in csv_reader:
        training_input = row[1:len(row)-1]
        training_inputs.append(training_input)
  return training_inputs

def generate_training_outputs(file_name: str) -> list:
  """
  Function to generate a list of training outputs
  :param: file_name: str
  :return: training_outputs: list
  """
  training_outputs = []
  with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    if header != None:
      for row in csv_reader:
        training_output = row[0]
        training_outputs.append(training_output)
  return training_outputs

def predict(predictor, test_set: list):
  outcome = predictor.predict(X=test_set)
  coefficients = predictor.coef_
  print('Predictions:', outcome)
  print('Coefficients:', coefficients)


def main():
  # Generate two output and input list from the csv file
  training_inputs_list = generate_training_inputs('SeoulBikeData.csv')
  training_outputs_list = generate_training_outputs('SeoulBikeData.csv')

  # Split the training input list into two list, training containing the first 80%, the remaining 20% are test
  training_inputs = training_inputs_list[0:int((len(training_inputs_list) - 1) * 0.8)]
  test_inputs = training_inputs_list[int((len(training_inputs_list) - 1) * 0.8) + 1:len(training_inputs_list)]

  # Split the training output list into two list, training containing the first 80%, the remaining 20% are test
  training_outputs = training_outputs_list[0:int((len(training_outputs_list) - 1) * 0.8)]
  test_outputs = training_outputs_list[int((len(training_outputs_list) - 1) * 0.8) + 1:len(training_outputs_list)]

  # Dit con me thang loz Do. Actually training the model.
  predictor = LinearRegression(n_jobs=-1)
  predictor.fit(X=training_inputs, y=training_outputs)
  predict(predictor, test_inputs)


main()