from background import get_stats_choice, check_choice

def option1():
  city_speed = int(input('Enter your average city driving speed (mph): '))
  highway_speed = int(input('Enter your average highway driving speed (mph): '))
  average_speed = city_speed + highway_speed / 2

  print(f'Your average driving speed is {average_speed} mph.\n')

def option2():
  # Calculate the average city speed limit
  general_city_speed = (10 + 25) / 2
  
  # Calculate the average highway speed limit
  general_highway_speed = (50 + 75) / 2
  
  general_speed = general_city_speed + general_highway_speed / 2
  user_speed = float(input('Enter your average speed: '))
  
  if user_speed > general_speed:
    speed_over = user_speed - general_speed
    print(f'\nYou drive {speed_over} mph over the general public speed limit.\n')
  elif user_speed < general_speed:
    speed_over = general_speed - user_speed
    print(f'\nYou drive {speed_over} mph under the general public speed limit.\n')
  else:
    print(f'\nYou drive the same speed as the general public speed limit.\n')

def option3():
  user_speed = float(input('Enter your average speed: '))
  user_overspeed = float(input('Enter how many miles over the speed limit: '))
  speed_40 = 0.15
  speed_50 = 0.59
  speed_55 = 0.78

  if user_speed < 50 and user_overspeed <= 5:
    fatal_chance = speed_40 + 0.03
  elif 50 <= user_speed < 55 and user_overspeed <= 5:
    fatal_chance = speed_50 + 0.03
  elif 55 <= user_speed <= 65 and user_overspeed <= 10:
    fatal_chance = speed_55 + 0.03
  elif 65 < user_speed <= 75 and user_overspeed <= 10:
    fatal_chance = speed_55 + 0.12
  else:
    fatal_chance = speed_55 + 0.13
  
  print(f'\nYour chance of possibly being fatally injured would be {fatal_chance}%\n')

def option4():
  age = int(input('How old are you? (Enter numbers only starting from 16): '))
  age_16 = 0.58
  age_20 = 0.57
  age_30 = 0.51
  age_40 = 0.32

  if 16 <= age <= 19:
    fatal_chance = age_16 + 0.14
  elif 20 <= age <= 29:
    fatal_chance = age_20 + 0.11
  elif 30 <= age <= 39:
    fatal_chance = age_30 + 0.07
  elif 40 <= age <= 49:
    fatal_chance = age_40 + 0.02
  else:
    fatal_chance = 0.24
  
  print(f'\nYour chance of possibly being fatally injured would be {fatal_chance}%\n')

def basic_stats():
  # Output title submenu
  # Output where data collected
  user_choice = ''

  while user_choice != 5:
    user_choice = get_stats_choice()

    if user_choice == 1:
      option1()
    # Check if user option is 2 then call the option2() function
    elif user_choice == 2:
      option2()
    # Check if user option is 3 then call the option3() function
    elif user_choice == 3:
      option3()
    # Check if user option is 4 then call the option4() function
    elif user_choice == 4:
      option4()
  
  # Check if the user chose to quit (option 5)
  if user_choice == 5:
    print('\nReturning to the main menu...\n')

def survey_analysis_choices():
  print('\n####################################################################################################################')
  print('\t\t\t\t\tDRIVING STATEMENT REPORT SURVEY ANALYSIS')
  print('\t\t\t\t\tData collected from Google Forms Survey\n\n')
  print('Choose one of the following numbered options to view statistics and visualizations about the vehicular accidents survey.\n')
  print('1. Histogram: Frequency Count from Linear Scale Question')
  print('2. Pie Chart: Distribution of Responses between Yes and No')
  print('3. Pie Chart: Distribution of Responses between Maybe and No')
  print('4. Pie Chart: Distribution of Responses between Yes and Maybe')
  print('5. Back to main menu\n')

  choice = check_choice(1, 5)

  return choice
