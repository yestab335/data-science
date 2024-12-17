import pandas as pd
from datacleaner import *
from visualizations import *
from ml import *
from models import high_complexity_model, low_complexity_model, cross_validation

def main():
  data = pd.read_csv('career_change_prediction_dataset.csv')
  data = data.drop(['Age', 'Gender', 'Certifications', 'Freelancing Experience', 'Geographic Mobility', 'Professional Networks', 'Technology Adoption'], axis=1)

  # View categorization fo the data
  print(data.info())

  # View the distribution of the target variable
  # histogram()
  # pie_chart(data['Likely to Change Occupation'].value_counts())
  # density()
  # scatter()
  # high_complexity_model()
  # low_complexity_model()
  # cross_validation()
  pairplot()

  # Apply mappings to columns
  # mappings = {
  #   'Field of Study': {
  #     'Medicine': 1,
  #     'Education': 2,
  #     'Arts': 3,
  #     'Computer Science': 4,
  #     'Business': 5,
  #     'Mechanical Engineering': 6,
  #     'Biology': 7,
  #     'Law': 8,
  #     'Economics': 9,
  #     'Psychology': 10,
  #   },
  #   'Current Occupation': {
  #     'Business Analyst': 1,
  #     'Economist': 2,
  #     'Biologist': 3,
  #     'Doctor': 4,
  #     'Lawyer': 5,
  #     'Software Developer': 6,
  #     'Artist': 7,
  #     'Psychologist': 8,
  #     'Teacher': 9,
  #     'Mechanical Engineer': 10,
  #   },
  #   'Education Level': {
  #     'High School': 1,
  #     'Bachelor\'s': 2,
  #     'Master\'s': 3,
  #     'PhD': 4,
  #   },
  #   'Industry Growth Rate': {
  #     'Low': 1,
  #     'Medium': 2,
  #     'High': 3,
  #   },
  #   'Family Influence': {
  #     'None': 1,
  #     'Low': 2,
  #     'Medium': 3,
  #     'High': 4,
  #   }
  # }

  # # Map the columns
  # for column, mapping in mappings.items():
  #   data[column] = data[column].map(mapping)

  # Split the data into training and testing
  features = data.drop('Likely to Change Occupation', axis=1)
  target = data['Likely to Change Occupation']
  x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, shuffle=True, random_state=42)

  knn_model(x_train, x_test, y_train, y_test, target)

if __name__ == '__main__':
  main()
