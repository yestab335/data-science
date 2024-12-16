import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, balanced_accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from confint import classification_confint
import plotly.graph_objects as go

data = pd.read_csv('career_change_prediction_dataset.csv')
data = data.drop(['Age', 'Gender', 'Certifications', 'Freelancing Experience', 'Geographic Mobility', 'Professional Networks', 'Technology Adoption'], axis=1)

fields_to_check = ['Field of Study', 'Current Occupation', 'Education Level', 'Industry Growth Rate', 'Family Influence', 'Likely to Change Occupation']
unique_values = {field: data[field].unique() for field in fields_to_check}

print(unique_values)

# Apply mappings to columns
mappings = {
  'Field of Study': {
    'Medicine': 1,
    'Education': 2,
    'Arts': 3,
    'Computer Science': 4,
    'Business': 5,
    'Mechanical Engineering': 6,
    'Biology': 7,
    'Law': 8,
    'Economics': 9,
    'Psychology': 10,
  },
  'Current Occupation': {
    'Business Analyst': 1,
    'Economist': 2,
    'Biologist': 3,
    'Doctor': 4,
    'Lawyer': 5,
    'Software Developer': 6,
    'Artist': 7,
    'Psychologist': 8,
    'Teacher': 9,
    'Mechanical Engineer': 10,
  },
  'Education Level': {
    'High School': 1,
    'Bachelor\'s': 2,
    'Master\'s': 3,
    'PhD': 4,
  },
  'Industry Growth Rate': {
    'Low': 1,
    'Medium': 2,
    'High': 3,
  },
  'Family Influence': {
    'None': 1,
    'Low': 2,
    'Medium': 3,
    'High': 4,
  }
}

# Map the columns
for column, mapping in mappings.items():
  data[column] = data[column].map(mapping)

# Check for NaN values introduced during mapping
nan_columns = data.columns[data.isnull().any()]
nan_info = {col: data[col].isnull().sum() for col in nan_columns}

print(nan_info)

data['Likely to Change Occupation'] = pd.to_numeric(data['Likely to Change Occupation'], errors='coerce')

print(data.head())

features = data.drop('Likely to Change Occupation', axis=1)
target = data['Likely to Change Occupation']
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, shuffle=True, random_state=42)

def high_complexity_model():
  global x_train
  global y_train
  global x_test
  dtree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=None, random_state=42)

  dtree.fit(x_train, y_train)

  pred_train = dtree.predict(x_train)
  pred_test = dtree.predict(x_test)

  print('\nHigh Complexity Model:')
  print('Train Accuracy: {:3.2f}'.format(accuracy_score(y_train, pred_train)))
  print('Test Accuracy: {:3.2f}'.format(accuracy_score(y_test, pred_test)))

  fig, ax = plt.subplots(1, 1, figsize=(9, 9), dpi=150)

  plot_tree(dtree, fontsize=4, filled=True, max_depth=3, feature_names=features.columns, class_names=['No', 'Yes'])
  plt.show()

def low_complexity_model():
  global x_train
  global y_train
  global x_test
  dtree = tree.DecisionTreeClassifier(criterion='entropy', max_depth=1, random_state=42)

  dtree.fit(x_train, y_train)

  pred_train = dtree.predict(x_train)
  pred_test = dtree.predict(x_test)
  
  print('\nLow Complexity Model:')
  print('Train Accuracy: {:3.2f}'.format(accuracy_score(y_train, pred_train)))
  print('Test Accuracy: {:3.2f}'.format(accuracy_score(y_test, pred_test)))

  fig, ax = plt.subplots(1, 1, figsize=(3, 3), dpi=150)

  plot_tree(dtree, fontsize=4, filled=True, max_depth=3, feature_names=features.columns, class_names=['No', 'Yes'])
  plt.show()

def cross_validation():
  # 5-Fold cross validation and shuffle the data
  cv = KFold(n_splits=5, shuffle=True)

  # Setting up grid search
  model = tree.DecisionTreeClassifier()
  param_grid = {
    'max_depth': list(range(1, 11)),
    'criterion': ['entropy', 'gini'],
  }
  grid = GridSearchCV(model, param_grid, cv=5)

  # Performing the grid search
  grid.fit(x_train, y_train)

  # Print the results
  print('Best Parameters: {}'.format(grid.best_params_))

  # Visualize the model
  fig, ax = plt.subplots(1, 1, figsize=(3, 3), dpi=150)

  plot_tree(grid.best_estimator_, fontsize=4, filled=True, max_depth=3, feature_names=features.columns, class_names=['No', 'Yes'])
  plt.show()

  # Prediction and accuracy
  pred_test = grid.best_estimator_.predict(x_test)

  print('Accuracy of optimal model: {:3.2f}'.format(accuracy_score(y_test, pred_test)))

  # Calculate the accuracy of the mode
  acc = grid.best_score_
  observations = x_test.shape[0]

  # 95% confidence interval
  lb, ub = classification_confint(acc, observations)

  print('Accuracy: {:3.2f} ({:3.2f}, {:3.2f})'.format(acc, lb, ub))

def model_metrics(y_true, y_predict):
  accuracy = accuracy_score(y_true, y_predict)
  precision = precision_score(y_true, y_predict, average='micro')
  recall = recall_score(y_true, y_predict, average='micro')
  f1 = f1_score(y_true, y_predict, average='micro')
  balanced_accuracy = balanced_accuracy_score(y_true, y_predict)

  return accuracy, precision, recall, f1, balanced_accuracy
