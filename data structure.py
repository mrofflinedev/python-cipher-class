# list datastructure
# ordered /indexes
# changeable/ mutables 

myproducts=["Bread","Milk","Sugar","Blueband"]
print(myproducts)


print(f"i like drinking tea that has {myproducts[1]} ")


# tuple datastructures
#ordered has indexes 
# unchangeable/immutable

countries=("Kenya","Tanzania","Burundi","Rwanda","Somalia")
print(countries)


# set datastructures
# non ordered
# avoids duplicates
computers={"hp","lenovo","dell","hp"}
print(computers)


#dictionary datastructures

customer={
        "name":"Collins",
        "Age":30,
        "city":"Kakamega",
        "salary":300000,
        "proffesion":"Software Engineer"
}
print(f"Customer Name : {customer['name']}")

myfruits=["mangoes","oranges","pineapples","watermelon","ovocado"]
for m in myfruits:
    print(f"i have {m}")

# imagine building a
# school system thatcalculates the average marks

marks=[65,89,64,89,90]
total=0
for x in marks:
    total=total+x
average=total /len(marks)
print(f"Total marks {total}")
print(f"Average marks: {average}")    

# create a complex calculator 
# using inputoutput and controlflows

print("Operations: +, -, *, /, %, **")

# loop to keep calculator running
while True:
    
    operator = input("Enter operator (+,-,*,/,%,**) or 'q' to quit: ").lower()

    if operator == "q":
        print("Calc terminated")
        break

    # --- TWO NUMBER OPERATIONS ---
    if operator in ["+", "-", "*", "/", "%", "**"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operator == "+":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operator == "-":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operator == "*":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operator == "/":
                if num2 != 0:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Cannot divide by zero!")
            elif operator == "%":
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            elif operator == "**":
                print(f"Result: {num1} ** {num2} = {num1 ** num2}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


    else:
        print("Invalid operator! Try again.")

     