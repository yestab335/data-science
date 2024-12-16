from background import *
from user_options import *
import pandas as pd

def main():
  fname = 'tabora_survey.csv'

  welcome_msg()

  # Flag variable keeping track of if the survey data has already been processed/cleaned
  #      assume at the beginning of program that survey data has NOT been processed/cleaned
  #      update this flag variable when the 5th or 7th option have been chosen for the first time
  survey_processed = False

  # Flag variable keeping track of if the DataFrame containing the data from your data set you found online 
  #      has already been processed/cleaned
  #      assume at the beginning of program that DataFrame has NOT been processed/cleaned
  #      update this flag variable when the 6th or 7th option have been chosen for the first time
  data_processed = False

  # Define string variable that is empty to hold user's input
  choice = ''

  # Loop until the user chooses the choice to quit the program
  while choice != 8:
    # Call the get_choice function to get the choice from the user and store in variable
    choice = get_choice()

    # Check if the user chose the first option
    if choice == 1:
      # Call overview function to output an overview of your topic
      overview()
    elif choice == 2:
      # Call question function to output the data-driven questions
      dq()
    elif choice == 3:
      # Call basic stats function to output the stats
      basic_stats()
    elif choice == 4:
      # Call simple visualizations function to output the data visualizations
      simple_visualizations()
    elif choice == 5:
      # Call survey analysis function to output the cleaned survey and visualizations
      if survey_processed == False:
        print('\n####################################################################################################################')
        print('\t\t\t\t\tPROCESSING AND CLEANING SURVEY DATA\n\n')
        print('One moment as the program cleans survey_responses.csv of data errors...\n')
        read_csv(fname)
        print('survey_responses.csv has been cleaned and processed.\n')
        survey_analysis()
        
        survey_processed = True
      else:
        survey_analysis()
    elif choice == 6:
      if data_processed == False:
        print('\n####################################################################################################################')
        print('\t\t\t\t\tPROCESSING AND CLEANING THE DATA SET\n\n')
        print('One moment as the program cleans Crash_Reporting_-_Drivers_Data.csv of data errors...\n')
        print('Uncleaned DataFrame has 172,105 rows.')
        print('Errors contained in this data set include:')
        print('1. Reformat the data set\'s columns into the proper data types.')
        print('2. Remove any missing values in the DataFrame.')
        print('3. Drop any duplicate rows in the DataFrame.')
        print('4. Reset the index after making all of these changes to the DataFrame.\n')
        print('Cleaned DataFrame has 104,410 rows.')
        print('Resolved data errors include:')
        print('1. Removed any rows with NaN (missing) values in the DataFrame.')
        print('2. Reformatted Unknown values to follow fomatting rules.')
        print('3. Reassigned the numeric data type to the Speed Limit column.')
        print('4. Dropped any duplicate rows in the DataFrame.')
        print('5. Reset the index of the DataFrame.\n')
        print('Crash_Reporting_-_Drivers_Data.csv has been cleaned and processed.')
        print('\n####################################################################################################################\n')
        process_df()

        data_processed = True
      else:
        process_df()
    elif choice == 7:
      data = 'vehicle_accidents.csv'
      df = read_as_dataframe(data)
      clean_df = clean_dataframe(df)
      findings(clean_df)
  if choice == 8:
    print('You have quit the program! Good day!')

if __name__ == '__main__':
  main()
