def greet():
    print("This is my first function")
greet()    
# function with parameters
def student(name,age,course):
    print(f"Student name is {name} ")
    print(f"Student age  is {age} ")
    print(f"Student course is {course} ")
student("Collins",21,"Software development")    
student("Esther",23,"Datascience")
student("Stephen",25,"Economics")
student("Rayvon",26,"Criminology")
student("Mercy",20,"Hospitality")
student("Ramah",35,"Education")


#function with return keyword
def add_number(a,b):
    return a+b
result=add_number(6,26)
print(f"Sum : {result}")

#create a function that will give you linear product
