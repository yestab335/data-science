import matplotlib.pyplot as plt
from background import check_choice
import numpy as np

def simple_visualizations_choices():
  print('\n####################################################################################################################')
  print('\t\t\tVEHICLE ACCIDENTS SIMPLE DATA VISUALIZATIONS ON FATALITY COUNT FROM RESULTING ACCIDENTS')
  print('\t\t\t\t\tData collected from NHTSA\n\n')
  print('Choose one of the following numbered options to view data visualizations about vehicular accidents.\n')
  print('1. Scatter Chart: Fatality Count by Year')
  print('2. Line Chart: Fatality Count by Year')
  print('3. Bar Chart: Fatality Count by Year')
  print('4. Pie Chart: Fatality Count by Year')
  print('5. Back to main menu\n')

  choice = check_choice(1, 5)

  return choice

def scatter_visual(list1, list2):
  fig, ax = plt.subplots()

  ax.scatter(list1, list2, label = 'Accident Count')

  # Set title and labels
  ax.set_title('Car Accident Fatality Count by Year')
  ax.set_xlabel('Years', fontsize = 10)
  ax.set_ylabel('Accident Count', fontsize = 10)

  # Add ticks
  ax.set_xticks(list1)
  ax.set_yticks(list2)

  # Add legend
  ax.legend()

  # Adjust layout
  fig.tight_layout()

  plt.show()

def line_visual(list1, list2):
  fig, ax = plt.subplots()

  ax.plot(list1, list2, label = 'Accident Count')

  # Set title and labels
  ax.set_title('Car Accident Fatality Count by Year')
  ax.set_xlabel('Years', fontsize = 10)
  ax.set_ylabel('Accident Count', fontsize = 10)

  # Add ticks
  ax.set_xticks(list1)
  ax.set_yticks(list2)
  
  # Add legend
  ax.legend()

  # Adjust layout
  fig.tight_layout()
  plt.show()

def bar_visual(list1, list2):
  fig, ax = plt.subplots()

  ax.bar(list1, list2, label = 'Accident Count')

  # Set title and labels
  ax.set_title('Car Accident Fatality Count by Year')
  ax.set_xlabel('Years', fontsize = 10)
  ax.set_ylabel('Accident Count', fontsize = 10)

  # Add ticks
  ax.set_xticks(list1)
  ax.set_yticks(list2)

  # Add legend
  ax.legend()

  # Adjust layout
  fig.tight_layout()
  plt.show()

def pie_visual(list1, list2):
  colors = plt.cm.Set3(range(len(list1)))

  plt.pie(list2, labels = None, autopct = '%1.1f%%', startangle = 140, colors = colors)
  plt.axis('equal')
  plt.title('Car Accident Fatality Count by Year')

  # Add legend
  plt.legend(loc = 'upper right', labels = list1)
  plt.show()

def minimum_val(list):
  minimum = list[0]
  
  for i in list:
    if i < minimum:
      minimum = i
  
  return minimum

def maximum_val(list):
  maximum = list[0]

  for i in list:
    if i > maximum:
      maximum = i
  
  return maximum

def average_val(list):
  total = 0
  count = 0

  for i in list:
    total += i
    count += 1
  
  average = total / count

  return average

def simple_visualizations():
  user_choice = ''
  yearKilled = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
  countKilled = [10_329, 9_696, 9_283, 9_723, 10_291, 9_947, 9_579, 9_592, 11_428, 12_330]
  minimum = minimum_val(countKilled)
  maximum = maximum_val(countKilled)
  average = average_val(countKilled)

  while user_choice != 5:
    user_choice = simple_visualizations_choices()

    if user_choice == 1:
      scatter_visual(yearKilled, countKilled)
      print(f'The minimum value is: {minimum}')
      print(f'The maximum value is: {maximum}')
      print(f'The average value is: {average}')
    # Check if user option is 2 then call the option2() function
    elif user_choice == 2:
      line_visual(yearKilled, countKilled)
      print(f'The minimum value is: {minimum}')
      print(f'The maximum value is: {maximum}')
      print(f'The average value is: {average}')
    # Check if user option is 3 then call the option3() function
    elif user_choice == 3:
      bar_visual(yearKilled, countKilled)
      print(f'The minimum value is: {minimum}')
      print(f'The maximum value is: {maximum}')
      print(f'The average value is: {average}')
    # Check if user option is 4 then call the option4() function
    elif user_choice == 4:
      pie_visual(yearKilled, countKilled)
      print(f'The minimum value is: {minimum}')
      print(f'The maximum value is: {maximum}')
      print(f'The average value is: {average}')
  
  # Check if the user chose to quit (option 5)
  if user_choice == 5:
    print('\nReturning to the main menu...\n')

def plt_linear_rating(integerRatingList):
  # Convert all elements in the list form strings to integers for numerical plotting
  integerRatingList = [int(value) for value in integerRatingList]

  # Plotting histogram
  plt.hist(integerRatingList, bins=3, color='skyblue', edgecolor='black')

  # Adding labels and title
  plt.xlabel('Values')
  plt.ylabel('Frequency')
  plt.title('Frequency Count of Responses from Linear Scale Question')

  # Displaying the plot
  plt.show()

def plt_counts(data, label1, label2):
  counts = {label1: 0, label2: 0}

  for item in data:
    if item == label1:
      counts[label1] += 1
    elif item == label2:
      counts[label2] += 1
  
  if counts[label1] != 0 or counts[label2] != 0:
    labels = list(counts.keys())
    sizes = list(counts.values())
    colors = ['lightcoral', 'lightskyblue']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Distribution of Responses from Multiple Choice Question')
  
    plt.show()
  else:
    print('No valid data to plot.')

def compute(linearScaleQuestionList):
  # Convert the strings in the list into floats to calculate the mean
  numeric_list = [1 if x == 'Yes' else 0 if x == 'No' else 0.5 for x in linearScaleQuestionList]

  # Mean
  mean = np.mean(numeric_list)

  return mean

# Function to create a summary table using groupby() method
def groupby_sum_table(df):
  # Group by 'Weather' and 'Surface Condition', and calculate the mean of 'Speed Limit'
  summary_table = df.groupby(['Weather', 'Surface Condition'])['Speed Limit'].mean().unstack(fill_value=0)

  # Reset index of the DataFrame
  df.reset_index(drop=True, inplace=True)

  return summary_table

# Function to create a summary table using pivot_table() method
def piv_sum_table(df):
  # Create a pivot table to analyze 'Weather' by 'Surface Condition'
  pivot_table = df.pivot_table(index='Weather', columns='Surface Condition', values='Report Number', aggfunc='count', fill_value=0)

  # Reset index of the DataFrame
  df.reset_index(drop=True, inplace=True)

  return pivot_table

# Function to create a scatter chart
def scatter_chart(df):
  y = df['Surface Condition']

  # Get unique surface conditions
  surface_conditions = y.unique()

  # Create a color map for surface conditions
  color_map = plt.cm.get_cmap('tab10', len(surface_conditions))

  # Create a scatter plot with different colors for each surface condition
  for i, surface_conditions in enumerate(surface_conditions):
    surface_df = df[y == surface_conditions]
    plt.scatter(surface_df['Weather'], surface_df['Surface Condition'], label=surface_conditions, color=color_map(i))
  
  plt.title('Scatter Plot of Weather vs Surface Condition')
  plt.xlabel('Weather')
  plt.ylabel('Surface Condition')
  plt.grid(True)

  # Rotate x-axis labels for better readability
  plt.xticks(rotation=45)

  # Add legend to identify each line
  plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
  
  # Adjust layout to prevent overlap of labels
  plt.tight_layout()
  plt.show()

# Function to create a line chart
def line_chart(pivot_table):
  plt.figure(figsize=(10, 6))

  for col in pivot_table.columns:
    plt.plot(pivot_table.index, pivot_table[col], marker='o', linestyle='-', label=col)
  
  plt.title('Line Chart of Weather vs Surface Condition')
  plt.xlabel('Weather Condition')
  plt.ylabel('Mean Speed Limit')

  # Rotate x-axis labels for better readability
  plt.xticks(rotation=45)

  # Add legend to identify each line
  plt.legend()

  # Adjust layout to prevent overlap of labels
  plt.tight_layout()
  plt.show()

# Function to create a bar chart
def bar_chart(df):
  # Group data by 'Weather' and count occurrences
  weather_counts = df['Weather'].value_counts()

  # Get unique colors for each bar
  num_bars = len(weather_counts)
  colors = plt.cm.tab10(np.linspace(0, 1, num_bars))

  # Create bar chart with different colors for each bar
  weather_counts.plot(kind='bar', color=colors)
  plt.title('Bar Chart of Weather Counts')
  plt.xlabel('Weather')
  plt.ylabel('Count')

  # Add gridlines only along the y-axis for better readability
  plt.grid(axis='y')

  # Rotate x-axis labels for better readabiliy
  plt.xticks(rotation=45)

  # Add legend to identify each line
  plt.legend(title='Value Counts')

  # Adjust layout to prevent overlap of labels
  plt.tight_layout()
  plt.show()

# Function to create a pie chart
def pie_chart(df):
  # Group data by 'Surface Condition' count occurrences
  grouped_data = df.groupby('Surface Condition').size()

  # Plotting the pie chart
  plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=140, labeldistance=1.1)
  plt.title('Pie Chart of Surface Condition Distribution')

  # Equal aspect ratio ensures that pie is drawn as a circle
  plt.axis('equal')

  # Adjust layout to prevent overlap of labels
  plt.tight_layout()

  # Add legend to identify each pie section
  plt.legend(title='Surface Conditions', loc='upper right')
  plt.show()
