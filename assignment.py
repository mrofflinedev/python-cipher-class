# Create a program that checks between 3 numbers which one is the biggest
 
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))

if num1 >= num2 and num1 >= num3:
      largest=num1
elif num2 >= num1 and num2 >= num3:
      largest=num2
else:
     largest=num3

print("The largest number is", largest)

# create a program that will perform addition,subtraction and division of 2 numbers
 
number1=float(input("Enter the first number"))
number2=float(input("Enter the second number"))
operator=input("Enter the operator(+,-,*,/)")

if operator == "+":
     print(f"the results of addition is: {number1 + number2}")
elif operator == "-":
     print(f"thr results of subtraction is: {number1 - number2}")
elif operator == "*":
     print(f"the results of multiplication is {number1 * number2}")
elif operator == "/":
     if number2 != 0:
          print(f"the results of division is: {number1 / number2}")
     else:
          print("cannot be divided by zero")
else:
    print("invalid operator")                   

#GRADE STUDENTS MARKS
#use the following grading system to grade students marks 70 and above = A, 60-69 = B, 50-59 = C, 40-49 = D, below 40 = Fail
marks = float(input("Enter marks (0-100): "))
if marks >=70:
     print(f"Grade A")
elif 60 <= marks <= 69:
     print(f"Grade B")
elif 50 <= marks <= 59:
     print(f"Grade C")
elif 40 <= marks <= 49:
    print("Grade D") 
else:
     print("Fail")

#ELECTRICITY BILL CALCULATOR
#WRITE A PROGRAM THAT CALCULATES THE ELECTRICITY BILL BASED ON THE NUMBER OF UNITS CONSUMED. THE BILLING RATES ARE AS FOLLOWS:
#- For the first 100 units: 25 per unit
#- For the next 100 units (101-200): 35 per unit
#- For the next 100 units (201-300): 45 per unit

units = float(input("Enter your units consumed (100-300):"))
if units == 100:
     print(f"25 per unit")
elif 101 <=units <=200:
     print(f"35 per unit")
else:
    print(f"45 per unit")     