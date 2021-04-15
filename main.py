import csv
import turtle
from sklearn.linear_model import LinearRegression

def generate_training_inputs(file_name: str, output_ind: int) -> list:
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
        training_input = [num != row[output_ind] for num in row]
        training_input = [float(i) for i in training_input]
        training_inputs.append(training_input)
  return training_inputs

def generate_training_outputs(file_name: str, output_ind: int) -> list:
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
        training_output = float(row[output_ind])
        training_outputs.append(training_output)
  return training_outputs

def predict(predictor, test_set: list):
  outcome = predictor.predict(X=test_set)
  coefficients = predictor.coef_
  print('Predictions:', outcome)
  print('Coefficients:', coefficients)
  return outcome

def calc_percentage_error(actual_val_list: list, predicted_val_list: list) -> dict:
  """
  Function to calculate the percentage errors
  :params: actual_val_list: list, predicted_val_list: list
  :return: percentage_error_dict: dict
  """
  percentage_error_dict = {
    '10%': 0,
    '10% - 20%':0,
    '20% - 30%': 0,
    '30% - 40%':0,
    '40% - 50%':0,
    '50% - 60%': 0,
    '60% - 70%':0,
    '70% - 80%':0,
    '80% - 90%':0,
    '90% - 100%': 0,
    '100% and above': 0
  }
  for i in range(len(actual_val_list) - 1):
    percentage_error = abs(actual_val_list[i] - predicted_val_list[i]) / actual_val_list[i]
    if percentage_error <= 10:
      percentage_error_dict['10%'] += 1
    if percentage_error > 10 and percentage_error <= 20:
      percentage_error_dict['10% - 20%'] += 1
    if percentage_error > 20 and percentage_error <= 30:
      percentage_error_dict['20% - 30%'] += 1
    if percentage_error > 30 and percentage_error <= 40:
      percentage_error_dict['30% - 40%'] += 1
    if percentage_error > 40 and percentage_error <= 50:
      percentage_error_dict['40% - 50%'] += 1
    if percentage_error > 50 and percentage_error <= 60:
      percentage_error_dict['50% - 60%'] += 1
    if percentage_error > 60 and percentage_error <= 70:
      percentage_error_dict['60% - 70%'] += 1
    if percentage_error > 70 and percentage_error <= 80:
      percentage_error_dict['70% - 80%'] += 1
    if percentage_error > 80 and percentage_error <= 90:
      percentage_error_dict['80% - 90%'] += 1
    if percentage_error > 90 and percentage_error <= 100:
      percentage_error_dict['90% - 100%'] += 1
    if percentage_error > 100:
      percentage_error_dict['100% and above'] += 1

  return percentage_error_dict
    

def drawBar(t, height):
  t.left(90)
  t.forward(height)
  t.right(90)
  t.forward(40)
  t.right(90)
  t.forward(height)
  t.left(90)

def main():
  file_name = input('Enter the name of your file (with .csv): ')
  output_ind = int(input('Enter the index of the output: '))

  # Generate two output and input list from the csv file
  training_inputs_list = generate_training_inputs(file_name, output_ind)
  training_outputs_list = generate_training_outputs(file_name, output_ind)

  # Split the training input list into two list, training containing the first 80%, the remaining 20% are test
  training_inputs = training_inputs_list[0:int((len(training_inputs_list) - 1) * 0.8)]
  test_inputs = training_inputs_list[int((len(training_inputs_list) - 1) * 0.8) + 1:len(training_inputs_list)]

  # Split the training output list into two list, training containing the first 80%, the remaining 20% are test
  training_outputs = training_outputs_list[0:int((len(training_outputs_list) - 1) * 0.8)]
  test_outputs = training_outputs_list[int((len(training_outputs_list) - 1) * 0.8) + 1:len(training_outputs_list)]

  # Dit con me thang loz Do. Actually training the model.
  predictor = LinearRegression(n_jobs=-1)
  predictor.fit(X=training_inputs, y=training_outputs)
  predicted_vals = predict(predictor, test_inputs)

  percentage_error_dict = calc_percentage_error(test_outputs, predicted_vals)

  xs = [i for i in percentage_error_dict.values()]  # here is the data
  maxheight = max(xs)
  numbars = len(xs)
  border = 10

  wn = turtle.Screen()             # Set up the window and its attributes
  wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
  wn.bgcolor("lightgreen")

  tess = turtle.Turtle()           # create tess and set some attributes
  tess.color("blue")
  tess.fillcolor("red")
  tess.pensize(3)

  for val in percentage_error_dict.values():
    drawBar(tess, val)
  
  wn.exitonclick()

if __name__ == '__main__':
  main()