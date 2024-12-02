import matplotlib.pyplot as plt
import seaborn as sns

def scatter(data, x, y, hueColor=None):
  x = x
  y = y

  sns.scatterplot(data=data, x=x, y=y, hue=hueColor)
  plt.title(f'{x} vs. {y}')
  plt.xlabel(x)
  plt.ylabel(y)
  plt.tight_layout()
  plt.show()
