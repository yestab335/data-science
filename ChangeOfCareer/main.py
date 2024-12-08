import pandas as pd
from datacleaner import *
from visualizations import *

def main():
  data = pd.read_csv('career_change_prediction_dataset.csv')

  # View categorization fo the data
  print(data.info())

  # View the distribution of the target variable
  histogram()
  scatter()
  density()

if __name__ == '__main__':
  main()
