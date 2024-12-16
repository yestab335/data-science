import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, balanced_accuracy_score, confusion_matrix
from sklearn.tree import plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from confint import classification_confint
from sklearn.svm import SVC

# kNN model
def knn_model(x_train, x_test, y_train, y_test, target_variable):
  model = KNeighborsClassifier()

  # 5-fold cross validation
  cv = KFold(n_splits=5, shuffle=True)

  # Grid search
  param_grid = {
    'n_neighbors': list(range(1, 26)),
  }

  grid = GridSearchCV(model, param_grid, cv=cv)

  # Performs the grid search
  grid.fit(x_train, y_train)

  print('Grid Search: best parameters: {}'.format(grid.best_params_))

  # Accuracy of best model with confidence interval
  pred_test = grid.best_estimator_.predict(x_test)
  acc = accuracy_score(y_test, pred_test)
  lb, ub = classification_confint(acc, x_test.shape[0])

  print('Accuracy: {:3.2f} ({:3.2f}, {:3.2f})'.format(acc, lb, ub))

  # Confusion matrix
  labels = list(target_variable.unique())
  cm = confusion_matrix(y_true=y_test, y_pred=pred_test, labels=labels)
  cm_df = pd.DataFrame(cm, index=labels, columns=labels)

  print('Confusion Matrix:\n{}'.format(cm_df))
