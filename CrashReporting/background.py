import csv
from visualizations import *
import pandas as pd
from user_options import survey_analysis_choices


def overview():
  print(
      '\n####################################################################################################################'
  )
  print('\t\t\t\t\tCrash_Reporting_-_Drivers_Data\n')
  print(
      'This CSV file contains a detailed report of vehicle crashes recorded by the Montgomery County Police and\nGaithersburg Police Department. Each entry includes information such as the report number, local case number,agency\nname, crash details (including date/time, location, weather, surface conditions, and light conditions), vehicle\ndetails (such as type, make, model, year, and damage extent), and various circumstances related to the crash\n(including driver distractions, driver substance abuse, traffic control, etc.). The file also includes details about\nrelated non-motorists involved in the crashes.'
  )
  print('')
  print(
      'Each row represents a unique crash report, and the columns include details such as the report number, local case\nnumber, agency name, ACRS report type, crash date and time, route type, road name, cross-street type, cross-street\nname, off-road description, municipality, related non-motorist involvement, collision type, weather conditions,\nsurface condition, lighting, traffic control measures, driver and non-motorist substance abuse, person ID, driver\nfault determination, injury severity, circumstances, driver distractions, driver\'s license state, vehicle ID,\nvehicle damage extent, vehicle impact locations, vehicle body type, vehicle movement, vehicle direction, speed limit,\ndriverless vehicle indication, parked vehicle indication, vehicle year, make, model, equipment problems, and\ngeographic coordinates of the crash location.'
  )
  print(
      '\n####################################################################################################################\n'
  )


def check_choice(minimum, maximum):
  # Define string variable that is empty to hold user's input
  some_input = ''

  # Loop until the user's input is no longer empty
  while some_input == '':
    # Ask the user to input their choice and store in a variable
    some_input = input('Choice: ')

    # Check if the user's input does not contain only digits
    if some_input.isdigit() == False:
      # Output an error message stating that the user did not enter input with only digits
      print('\nYou did not enter input with only digits! Try again.\n')

    # Otherwise (i.e., the user's input contains only digits)
    else:
      # Convert the user's input to an integer
      # '1' --> 1
      some_input = int(some_input)

      # Check if the user's input is less than the minimum or greater than the maxiumum
      if some_input < minimum or some_input > maximum:
        # Output an error message stating that the user did not enter input between 1 and 5
        print('\nYou did not enter a valid choice. Choose any option from ' +
              str(minimum) + ' to ' + str(maximum) + '.\n')

  # Return the user's input
  return some_input


def get_choice():
  # Output the list of options the user can choose from
  # Choice 1 --> Overview of the Crash_Reporting_-_Drivers_Data Data Set
  # Choice 2 --> Data-Driven Questions and Predictions
  # Choice 3 --> Basic Statistics on Crash_Reporting_-_Drivers_Data
  # Choice 4 --> Simple Data Visualizations on Crash_Reporting_-_Drivers_Data
  # Choice 5 --> Survey Analysis
  # Choice 6 --> Data Set Analysis
  # Choice 7 --> Findings and Observations
  # Choice 8 --> Quit
  print(
      'Choose one of the options below to view the data analysis for this data set and its data-driven question.\n'
  )

  print('1. Overview of the Crash_Reporting_-_Drivers_Data Data Set')
  print('2. Data-Driven Questions and Predictions')
  print('3. Basic Statistics on Crash_Reporting_-_Drivers_Data')
  print('4. Simple Data Visualizations on Crash_Reporting_-_Drivers_Data')
  print('5. Survey Analysis')
  print('6. Data Set Analysis')
  print('7. Findings and Observations')
  print('8. Quit.\n')

  # Call the check_choice function passing it 1 as the minimum and 8 as the maximum
  #      store the returned value in a variable
  choice = check_choice(1, 8)

  # Rreturn the user's input that was stored in the variable above
  return choice


def welcome_msg():
  dq = 'Does different weather conditions contribute to more accidents?'

  print('\t\t\t\t\tCrash_Reporting_-_Drivers_Data: ')
  print('\t\t\t\t' + dq.upper())
  print('\n')
  print(
      '\t\t\tWelcome to the Crash_Reporting_-_Drivers_Data data set analysis program!\n'
  )


def dq():
  print(
      '\n####################################################################################################################'
  )
  print('\t\t\t\t\tDATA-DRIVEN QUESTIONS AND PREDICTIONS\n')
  print(
      'Question #1: Does different weather conditions contribute to more accidents?\n'
  )
  print(
      'Prediction: Different weather conditions play a role into the contribution of an increase in car accidents.\n\n'
  )
  print(
      'Question #2: Do different speed limits contribute to more accidents?\n')
  print(
      'Prediction: The faster the speed limit the more dangerous the roadways are and leads to an increase in the number of car accidents.'
  )
  print(
      '\n####################################################################################################################\n'
  )


def get_stats_choice():
  print(
      '\n####################################################################################################################'
  )
  print('\t\t\t\t\tVEHCILE ACCIDENTS BASIC DATA STATISTICS')
  print('\t\t\t\t\tData collected from NHTSA\n\n')
  print(
      'Choose one of the following numbered options to view data and statistics about car crashes:\n'
  )
  print('1 - Calculate your average driving speed')
  print(
      '2 - Find out how much faster you drive from the general average speed limit'
  )
  print('3 - Find the likelihood of getting fatally injured by speed')
  print('4 - Find the likelihood of getting fatally injured by age')
  print('5 - Back to main menu\n')

  choice = check_choice(1, 5)

  return choice


def read_csv(filename):
  cleanedLinearQuestionList = []
  cleanedMultipleQuestionList = []
  lChoice1_count = 0
  lChoice2_count = 0
  lChoice3_count = 0
  mChoice1_count = 0
  mChoice2_count = 0
  mChoice3_count = 0

  with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
      if row['Rate your driving on a scale of 1 - 7'] == '' or row[
          'Rate your driving on a scale of 1 - 7'] == None:
        print(f'Error in line {reader.line_num}. Value is missing')
      else:
        cleanedLinearQuestionList.append(
            row['Rate your driving on a scale of 1 - 7'])

        if 'Yes' in row['Rate your driving on a scale of 1 - 7']:
          lChoice1_count += 1
        elif 'No' in row['Rate your driving on a scale of 1 - 7']:
          lChoice2_count += 1
        elif 'Maybe' in row['Rate your driving on a scale of 1 - 7']:
          lChoice3_count += 1

    # Reset the file pointer to the beginning of the file
    csvfile.seek(0)

    for rows in reader:
      if rows[
          'Are you distracted while driving (i.e. are you on your phone when you drive or play with the radio)?'] == '' or rows[
              'Are you distracted while driving (i.e. are you on your phone when you drive or play with the radio)?'] == None:
        print(f'Error in line {reader.line_num}. Value is missing')
      else:
        cleanedMultipleQuestionList.append(rows[
            'Are you distracted while driving (i.e. are you on your phone when you drive or play with the radio)?']
                                           )

        if 'Yes' in rows[
            'Are you distracted while driving (i.e. are you on your phone when you drive or play with the radio)?']:
          mChoice1_count += 1
        elif 'No' in rows[
            'Are you distracted while driving (i.e. are you on your phone when you drive or play with the radio)?']:
          mChoice2_count += 1
        elif 'Maybe' in rows[
            'Are you distracted while driving (i.e. are you on your phone when you drive or play with the radio)?']:
          mChoice3_count += 1

  return cleanedLinearQuestionList, cleanedMultipleQuestionList


def check_age(some_age):
  valid = True

  if some_age.isdigit() or some_age[0:2].isdigit():
    if len(some_age) > 2 and some_age[2].isdigit():
      age = int(some_age[0:3])
    else:
      age = int(some_age[0:2])

    if age < 0 or age > 150:
      valid = False
  else:
    valid = False

  return valid


def check_linear_scale(user_rating):
  valid = True

  if user_rating > 7 or user_rating < 1:
    valid = False

  return valid


def check_multiple_choice(user_response):
  valid = True

  if not ('') in user_response:
    valid = True
  else:
    valid = False

  return valid


# Function to read the CSV file and return it as a DataFrame
def read_as_dataframe(filename):
  dtype_dict = {
      'Report Number': 'str',
      'Local Case Number': 'str',
      'Agency Name': 'str',
      'ACRS Report Type': 'str',
      'Crash Date/Time': 'str',
      'Route Type': 'str',
      'Road Name': 'str',
      'Cross-Street Type': 'str',
      'Cross-Street Name': 'str',
      'Off-Road Description': 'str',
      'Municipality': 'str',
      'Related Non-Motorist': 'str',
      'Collision Type': 'str',
      'Weather': 'str',
      'Surface Condition': 'str',
      'Light': 'str',
      'Traffic Control': 'str',
      'Driver Substance Abuse': 'str',
      'Non-Motorist Substance Abuse': 'str',
      'Person ID': 'str',
      'Driver At Fault': 'str',
      'Injury Severity': 'str',
      'Circumstance': 'str',
      'Driver Distracted By': 'str',
      'Drivers License State': 'str',
      'Vehicle ID': 'str',
      'Vehicle Damage Extent': 'str',
      'Vehicle First Impact Location': 'str',
      'Vehicle Second Impact Location': 'str',
      'Vehicle Body Type': 'str',
      'Vehicle Movement': 'str',
      'Vehcile Continuing Dir': 'str',
      'Vehicle Going Dir': 'str',
      'Speed Limit': 'int',
      'Driverless Vehicle': 'str',
      'Parked Vehicle': 'str',
      'Vehicle Year': 'int',
      'Vehicle Make': 'str',
      'Vehicle Model': 'str',
      'Equipment Problems': 'str',
      'Latitude': 'float64',
      'Longitude': 'float64',
      'Location': 'str',
  }

  # Read the CSV file into a DataFrame
  file = pd.read_csv(filename, dtype=dtype_dict)

  # Convert the file into a DataFrame
  df = pd.DataFrame(file)

  return df


# Function to clean the DataFrame
def clean_dataframe(df):
  # Drops all missing values within the specified subsets
  df.dropna(subset=[
      'Parked Vehicle', 'Surface Condition', 'Weather', 'Light',
      'Traffic Control', 'Driver Substance Abuse'
  ],
            inplace=True)

  # Drops all duplicate rows within the entire dataframe
  df.drop_duplicates()

  # Replace 'Unknown' values in the 'Weather' column with 'UNKNOWN'
  df['Weather'] = df['Weather'].replace('Unknown', 'UNKNOWN')

  # Convert 'Speed Limit' column to numeric type
  df['Speed Limit'] = pd.to_numeric(df['Speed Limit'])

  # Drop unnesessary columns from the DataFrame
  df = df.drop(columns=[
      'Report Number', 'Local Case Number', 'Agency Name', 'ACRS Report Type',
      'Crash Date/Time', 'Route Type', 'Road Name', 'Cross-Street Type',
      'Cross-Street Name', 'Off-Road Description', 'Municipality'
  ])

  # Reset index of the DataFrame
  df.reset_index(drop=True, inplace=True)

  return df


# Function to get a subset of the DataFrame based on 'Weather' condition
def get_subset(df):
  df_subset = df[df['Weather'] == 'CLEAR']

  return df_subset

def survey_analysis():
  user_choice = ''
  fname = 'survey.csv'
  linearQuestionList, multipleQuestionList = read_csv(fname)
  mean = compute(multipleQuestionList)

  while user_choice != 5:
    user_choice = survey_analysis_choices()

    if user_choice == 1:
      plt_linear_rating(linearQuestionList)
      print(f'The mean is {mean}')
    elif user_choice == 2:
      plt_counts(multipleQuestionList, 'Yes', 'No')
      print(f'The mean is {mean}')
    elif user_choice == 3:
      plt_counts(multipleQuestionList, 'No', 'Maybe')
      print(f'The mean is {mean}')
    elif user_choice == 4:
      plt_counts(multipleQuestionList, 'Yes', 'Maybe')
      print(f'The mean is {mean}')
  
  if user_choice == 5:
    print('\nReturning to the main menu...\n')


# Function for conducting data analysis on vehicle accidents dataset
def data_analysis():
  print(
      '\n####################################################################################################################'
  )
  print('\t\t\t\t\tVEHICLE ACCIDENTS DATA SET ANALYSIS')
  print('\t\t\t\t\tData collected from Data.gov Data Repository\n\n')
  print(
      'Choose one of the following numbered options to view pivot tables and visulizations about the vehicular accidents data set.\n'
  )
  print(
      '1. Summary Table: Weather and Surface Condition Accident Count with Respective Speed Limit'
  )
  print('2. Pivot Table: Weather and Surface Conditions')
  print('3. Scatter Chart: Weather vs Surface Condition')
  print('4. Line Chart: Weather vs Surface Condition')
  print('5. Bar Chart: Weather Accident Count')
  print('6. Pie Chart: Surface Condition Accident Count Distribution')
  print('7. Back to main menu\n')

  choice = check_choice(1, 7)

  return choice


# Function for processing the data
def process_df():
  user_choice = ''
  data = 'vehicle_accidents.csv'
  df = read_as_dataframe(data)
  clean_df = clean_dataframe(df)

  while user_choice != 7:
    user_choice = data_analysis()

    if user_choice == 1:
      summary_table = groupby_sum_table(clean_df)
      print(summary_table)
    elif user_choice == 2:
      pivot_table = piv_sum_table(df)
      print(pivot_table)
    elif user_choice == 3:
      scatter_chart(clean_df)
    elif user_choice == 4:
      pivot_table = piv_sum_table(df)
      line_chart(pivot_table)
    elif user_choice == 5:
      bar_chart(clean_df)
    elif user_choice == 6:
      pie_chart(clean_df)

  if user_choice == 7:
    print('\nReturning to the main menu...\n')


# Function for the results of the data endeavour
def findings(clean_df):
  # Define requested variables for the data analysis
  yearKilled = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
  countKilled = [
      10_329, 9_696, 9_283, 9_723, 10_291, 9_947, 9_579, 9_592, 11_428, 12_330
  ]
  minimum = minimum_val(countKilled)
  maximum = maximum_val(countKilled)
  average = average_val(countKilled)
  df = read_as_dataframe('vehicle_accidents.csv')

  print(
      '\n####################################################################################################################'
  )
  print('\t\t\t\t\tANSWERS TO DATA-DRIVEN QUESTIONS\n\n')
  print(
      'Question #1: Does different weather conditions contribute to more accidents?\n'
  )
  print(
      'Prediction: Different weather conditions play a role into the contribution of an increase in car accidents.\n\n'
  )
  print(
      'Observation(s): The number of vehicle accidents are increasing over time.\n'
  )
  print(
      'Over a span of nine years, from 2012 to 2021, data from the National Highway Traffic Safety Administration reveals a\nnotable trend: the recorded number of vehicular accidents has risen from 10,329 to 12,330. This represents a\nsignificant increase of 2,001 accidents during this period.\n'
  )
  print(
      'Moreover, by visualizing the dataset of vehicle accidents gathered from the NHTSA spanning from 2012 to 2021, a\ndiscernible pattern emerges: there has been a consistent upward trajectory in these incidents over the past nine\nyears, culminating in the highest recorded count observed in 2021.\n'
  )

  line_visual(yearKilled, countKilled)

  print(f'\nThe minimum value is: {minimum}')
  print(f'The maximum value is: {maximum}')
  print(f'The average value is: {average}\n')
  print(
      'It is widely acknowledged that varying weather conditions yield distinct levels of traction for vehicles. At the\noutset of this research endeavor, I harbored the preliminary hypothesis that inclement weather and adverse surface\nconditions, characterized by moisture, darkness, and weightiness, would likely correlate with a higher incidence of\nvehicular accidents. This supposition was informed by a natural inclination towards speculating on the potential\nimpacts of particular weather phenomena on driving safety.\n'
  )
  print(
      'Although vehicular accidents persist during snowy, rainy, and sleet weather conditions, predominantly on wet roads,\nit is noteworthy that a higher incidence of such accidents occurs under clear weather conditions with dry roads.\n'
  )

  bar_chart(clean_df)

  print(
      'Question #2: Do different speed limits contribute to more accidents?\n')
  print(
      'Prediction: The faster the speed limit the more dangerous the roadways are and leads to an increase in the number\nof vehicle accidents.\n\n'
  )
  print(
      'Observation(s): The role of speed in vehicular accidents is recognized as both primary and secondary, exerting\nsignificant influence on the resulting outcomes.\n'
  )
  print(
      'It is customary to posit that higher speeds correlate with a heightened frequency of vehicular accidents. This\ncorrelation arises from the understanding that increased velocity extends the braking distance of vehicles and\nreduces the available reaction time to unforeseen or unusual circumstances.\n'
  )
  print(
      'While this assertion holds validity in certain instances, it is important to recognize that speed primarily\nfunctions as a secondary factor in the occurrence of vehicular accidents. Its impact is intricately intertwined\nwith weather and surface conditions, as illustrated in the summary table provided below:\n'
  )

  print(groupby_sum_table(clean_df))

  print(
      '\nIt is worth noting from the summary table that the incidence of accidents predominantly arises during periods\nof relatively low speeds across various weather and surface conditions.\n'
  )

  line_chart(piv_sum_table(df))

  print(
      '\nAs evidenced by the line chart, a significant proportion of vehicular accidents occur under conditions\ncharacterized by low speeds, clear weather, and dry surface conditions.\n'
  )
  print(
      'In summary, both speed and various weather conditions indeed exert notable influences on the occurrence\nof vehicular accidents, albeit not necessarily in the anticipated manner. Contrary to initial\nassumptions regarding higher speeds and adverse weather conditions such as snow, rain, or sleet leading\nto elevated accident counts, the findings indicate a different pattern. It emerges that the highest\nincidence of accidents transpires under conditions characterized by clear weather, dry surfaces, and\nlower speed limits, offering insights that deviate from the initial expectations.\n'
  )
