
# Using script mode write a program that will output the text “Hello There” to screen

print('Hello There')


# Create a String variable to store your name and an int variable to store your age. Print this out to screen using the Script mode.

name = 'John Example'
age = 30
print('Name:',name,' age:',age)


# Write a program that will ask a student for their first name and then for their surname.
# It should then ask the student to enter the int numerical grade they received in each of their three subjects.
# The program should then print out the full name of the student along with their average numerical grade (Use only a single print statement)

firstName = input('Enter your first name: ')
surname = input('Enter your surname: ')
numberOfSubjectsInputed = int(input('Number of subjects: '))

def countGradesAverage(numberOfSubjects):
  totalGrades = 0
  for grade in range(numberOfSubjects):
    singleGrade = float(input('Grade of the {} subject: '.format(grade+1)))
    totalGrades += singleGrade

  gradesAverage = totalGrades/numberOfSubjects
  return gradesAverage

print('Hi {} {},\nYour average is'.format(firstName, surname), countGradesAverage(numberOfSubjectsInputed))


# Write a program that asks the user to enter a distance in kilometres and then converts that distance to miles (Miles = Kilometres * 0.6214).

def convertToMiles(kilometers):
  miles = kilometers * 0.6214
  print(kilometers,'kilometers is',miles,'miles.')

convertToMiles(float(input('Enter distance in kilometers: ')))


# Write a program to calculate and display a person’s body mass index (BMI).
# A persons BMI is calculated with the following formula: BMI = (weight/height**2 ) * 703,
# where weight in in pounds and height in in inches. Your program should ask the user for their weight (in pounds) and height (in inches).

def calculateBMI(weight, height):
  BMI = (weight/height**2)*703
  print('Your BMI is', BMI)

weightInput = float(input('Enter your weight: '))
heightInput = float(input('Enter your height: '))
calculateBMI(weightInput, heightInput)

# There are three seating categories at a stadium.
# For a football games, Class A seat’s cost €25, Class B seat’s cost €20 and Class C seat’s cost €30.
# Write a program that asks how many tickets for each class of seats were sold, and then display the amount of income generated from ticket sales.

aSeatCost = 25
bSeatCost = 20
cSeatCost = 30

aTicketsNumber = int(input('Number of Class A tickets sold: '))
bTicketsNumber = int(input('Number of Class B tickets sold: '))
cTicketsNumber = int(input('Number of Class C tickets sold: '))

totalIncome = float(aSeatCost * aTicketsNumber + bSeatCost * bTicketsNumber + cSeatCost * cTicketsNumber)
print('Income generated: €{}'.format(totalIncome))