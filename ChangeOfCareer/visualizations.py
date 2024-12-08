import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('career_change_prediction_dataset.csv')

def scatter():
  fig, ax = plt.subplots(1, 2, figsize=(12, 5))
  x1 = data['Years of Experience']
  y1 = data['Job Satisfaction']
  x2 = data['Salary']
  y2 = data['Job Opportunities']
  hue_color = data['Likely to Change Occupation']

  # Left scatter plot
  sns.scatterplot(data=data, x=x1, y=y1, hue=hue_color, ax=ax[0])
  ax[0].set_title('Years of Experience vs. Job Satisfaction')

  sns.scatterplot(data=data, x=x2, y=y2, hue=hue_color, ax=ax[1])
  ax[1].set_title('Salary vs. Job opportunities')

  plt.tight_layout()
  plt.show()

def density():
  fig, ax = plt.subplots(1, 2, figsize=(12, 5))
  global data

  # Density plot of Years of Experience distribution
  sns.kdeplot(data[data['Likely to Change Occupation'] == 'Yes']['Years of Experience'], fill=True, label='Yes', ax=ax[0])
  sns.kdeplot(data[data['Likely to Change Occupation'] == 'No']['Years of Experience'], fill=True, label='No', ax=ax[0])
  ax[0].set_title('Density Plot of Years of Experience by Likely to Change Occupation')

  # Density plot of Job Satisfaction distribution
  sns.kdeplot(data[data['Likely to Change Occupation'] == 'Yes']['Job Satisfaction'], fill=True, label='Yes', ax=ax[1])
  sns.kdeplot(data[data['Likely to Change Occupation'] == 'No']['Job Satisfaction'], fill=True, label='No', ax=ax[1])
  ax[1].set_title('Density Plot of Job Satisfaction by Likely to Change Occupation')

  plt.legend()
  plt.show()

def histogram():
  global data

  plt.hist(data['Likely to Change Occupation'])
  plt.tight_layout()
  plt.show()
