import math
def choice():
  #gets userinput regarding if they want to lose or gain weight 
  global fitness_choice
  fitness_choice = input("Do you want to lose fat or build muscle? \n") 
  if fitness_choice == "build muscle":
    print("It's great that you want to bulk up with some muscle! Let's get on the grind! \n") 
  elif fitness_choice == "lose fat":
    print("It's great that you are trying to slim down by cutting fat! Let's get on the grind! \n")

def calculate_BMI():
  #calculates the bmi based on age, height, and weight
  global age
  age = int(input("What is your age in years? \n")) 
  height_squared = math.pow(height, 2)
  global BMI
  BMI = (weight/height_squared)*703
  print("Your current BMI is " + str(round(BMI, 2)))

def evaluate_BMI(): 
  #evaluates the bmi if the user is underweight, normal weight, or overweight
  if 0 < BMI <= 18.4:
    print("You're pretty underweight, let's pack on some muscle! \n") 
  elif 18.5 <= BMI <= 24.9:
    print("You're maintaining a healthy weight, great job! \n")
    choice()
  elif BMI >= 25:
    print("You're pretty overweight, let's shred some fat! \n")

def calculate_basal_metabolic_rate(weight, height, gender): 
  #calculates the basal metabolic rate based on weight, height, and gender
  kilograms = weight/2.2
  centimeters = height*2.54
  global basal_metabolic_rate
  if gender == "male":
    basal_metabolic_rate = int(66.5 + (13.75*kilograms) + (5.003*centimeters) - (6.755*age))
  else:
    basal_metabolic_rate = int(655.1 + (9.56*kilograms) + (1.85*centimeters) - (4.67*age))
#Basal Metabolic Rate is based upon the Benedict Harris Equation

def calculate_maintenance_calories():
  #calculates the number of calories needed to lose/gain the specified amount of weight 
  #based on the user's activity level and basal metabolic rate
  activity_list = ["Sedentary", "Light Activity", "Moderate Exercise", "Active", "Very Active"]           
  activity_level = input("Choose your activity level: " + str(activity_list) + " ")
  global basal_metabolic_rate
  if activity_level == "Sedentary":
    basal_metabolic_rate *= 1.1
  if activity_level == "Light Activity": 
    basal_metabolic_rate *= 1.3
  if activity_level == "Moderate Exercise": 
    basal_metabolic_rate *= 1.5
  if activity_level == "Active": 
    basal_metabolic_rate *= 1.7
  if activity_level == "Very Active": 
    basal_metabolic_rate *= 2
  weight_loss = float(input("How many pounds do you want to lose/gain a week? ")) 
  calorie_loss = (100 * weight_loss)
  global fitness_choice
  fitness_choice = " "
  if fitness_choice == "lose fat" or BMI >= 25:
    print("If you want to lose " + str(weight_loss) + " pounds every week, then you need to eat "
    + str(int(basal_metabolic_rate - (calorie_loss))) + " calories from your diet everyday.") 
  else:
    print("If you want to gain " + str(weight_loss) + " pounds every week, then you need to eat " + str(int(basal_metabolic_rate + (100*weight_loss))) + " calories from your diet everyday.")
    print("Your maintenance level calories are " + str(int(basal_metabolic_rate)))


#controls logic flow of the program
print("Welcome to the beginning of your Fitness Journey!") 
print('"A journey of a thousand miles begins with a single step..."') 
#collects user biometrics
weight = int(input("What is your weight in pounds? \n"))
height = int(input("What is your height in inches? \n"))
gender = input("Are you a male or female? \n")
#calls functions in flow of the program
calculate_BMI()
evaluate_BMI() 
calculate_basal_metabolic_rate(weight, height, gender) 
calculate_maintenance_calories()