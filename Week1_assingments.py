# Question 1:
## Write a program that converts a temperature from Celsius to Fahrenheit.
## (Formula: Fahrenheit = (Celsius * 9/5) + 32) 

celsius = 25  # Value of celsius
fahrenheit = (celsius * 9/5) + 32 # Formula 
print(f"{celsius}°C is equal to {fahrenheit}°F") # output  the result



# Question 2:
# Calculate Area of a Rectangle
Lenght = 8
Widht = 15
area = Lenght * Widht  # Area formula
print(f"The area of the rectangle is {area} square units")  # output the result



# Question 3:
# Calculate Compound Interest Use the formula: CI = P * (1 + R/100)**T - P 
# Where P = principal, R = rate, T = time
Principal = 1000    # principal amount
Rate = 5           # rate of interest
Time = 2           # time in years
compound_interest = Principal * (1 + Rate / 100) ** Time - Principal
print(f"the compound interest is {compound_interest}")  # output the result



# Question 4: 
# Perimeter of a Rectangle - Take length and width as input and calculate the perimeter
# perimeter = 2 * (length + width)
length = 10  # Length of the rectangle
width = 5    # Width of the rectangle
perimeter = 2 * (length + width)  # Perimeter formula
print(f"The perimeter of the rectangle is {perimeter} units")  # output the result



# Question 5:
#Average of Three Numbers - Input three numbers and print their average. 
num1 = 10  # First number
num2 = 20  # Second number  
num3 = 30  # Third number
average = (num1 + num2 + num3) / 3  # Average formula
print(f"The average of {num1}, {num2}, and {num3} is {average}")  # output the result



# Question 6:
# Square and Cube of a Number - Ask the user for a number and display its square and cube

number = 65  # Input a number
square = number ** 2 # Calculate square
cube = number ** 3 
print(f"the square of the number is {square} and the cube is {cube}") # output the result



# Question 7:
#Distribute Items Equally - You have n candies and k students.
#  Write a program to find:
#  how many candies each student gets
#  how many are left 
n= 50  # number of candies 
k = 29  # number of students
candies_per_student = n//k
remaining_candies = n % k
print(f"Each student gets {candies_per_student} candies and {remaining_candies} candies are left.")  # output the result



# Question 8:
#Calculate Profit or Loss
#Input cost price and selling price. Display either:
# Profit and amount, or Loss and amount, or
#No Profit No Loss
cost_price = 5000
selling_price = 5500
if cost_price < selling_price:
   profit_amount= selling_price - cost_price
   print("You are in Profit")
   print("profit amount =",profit_amount)
elif cost_price > selling_price:
   loss_amount = cost_price - selling_price
   print("you are in Loss")
   print("loss amount =",loss_amount)
else:
   print("No Profit No Loss")
   
# Question 9:
# Total Marks and Percentage ::::::::::::::::
# Input marks of 5 subjects. Print:::::::::::::::::: 
#  Total marks :::::::::::::::::::
#  Percentage ::::::::::::::::::::
#  Average::::::::::::::::::
marks = 500
dict = {
   "Math" : 85,
   "science" : 90,
   "English" : 99,
    "History" : 88,
    "Geography" : 92
   }
Total_marks = sum(dict.values())
Percentage = (Total_marks / marks) * 100
Average = Total_marks / 5
print(Total_marks)
print(Percentage)
print(Average)

# Question 10:
# Salary Calculator 
# Input basic salary. Calculate: 
#  HRA = 20% of basic 
#  DA = 15% of basic 
#  Total Salary = Basic + HRA + DA 

basic_salary = 50000
HRA = 0.20 * basic_salary
DA = 0.15 * basic_salary
total_salary = basic_salary + HRA + DA
print(f"Basic Salary: {basic_salary}")





