import matplotlib.pyplot as plt
import seaborn as sns

plt.subplots(1, 1, figsize=(12, 6))

def scatter(data, x, y, hueColor=None):
  sns.scatterplot(data=data, x=x, y=y, hue=hueColor)
  plt.tight_layout()
  plt.show()

def density(data):
  sns.kdeplot(data)
  plt.show()

def histogram(distVariable, density=None):
  plt.hist(distVariable, density=density)
  plt.tight_layout()
  plt.show()
