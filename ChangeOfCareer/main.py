import pandas as pd
from datacleaner import *
from visualizations import *
import matplotlib.pyplot as plt

def main():
  data = pd.read_csv('career_change_prediction_dataset.csv')

  # View categorization fo the data
  print(data.info())

  # View the distribution of the target variable
  # plt.subplots(1, 1, figsize=(12, 6))

  histogram(data['Current Occupation'], True)
  plt.title('Figure 1. Data Distribution of Target Variable')

  # TODO: Carrer Change Interest - reassign 1 to yes and 0 to no
  # data['Career Change Interest'] = data['Career Change Interest'].map({
  #   0: 'No',
  #   1: 'Yes',
  # })

if __name__ == '__main__':
  main()
