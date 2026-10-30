# for loop
for i in range(1,11):
    print(f"Welcome to my shop!Customer {i} ")
customers=["Collins","Erick","Samuel","Esther","Stephen","Gloria","Ramah","Joseck","Faith","Mercy"]
for c in customers:
    print(f"Welcome to todays class! {c} ")

# calculate expense that you bought 
# bread ksh90
# milk  ksh120
# sugar ksh 160
my_shopping=[90,120,160]
total=0
for m in my_shopping:
    total=total+m
    print(f"My totalshopping cost is {total}")

# imagine you have five
# customers and each pay you 100. create a
# script to get the total      

for i in range(1,6):
 customers=["customer1","customer2","customer3","customer4","customer5"]
payments=[100,100,100,100,100]
total=0
for m in payments:
    total=total+m
    print(f"total payment is {total}")

#alternative
total=0
for num in range(1,6):
   total=total+100
print(f"Total money collected : ksh {total}")



#while loop
x=0
while x<=10:
   print(f"Loops {x}")
   x+=1
# imagine you want to save starting with 0 balance  
# and save 100 daily until you have 1000.

money=0
while money<1000:
   money=money+100
   #money+=100 (this is same as above expression)
   print(f"Money saved: {money}") 
print(f"Congratulations! you have reached your target")

