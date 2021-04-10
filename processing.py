import csv

def main():
  read_file = open("SeoulBikeData.csv", "r")
  csv_file = csv.reader(read_file)
    
  for line in csv_file:
    print(line)



main()