#check the number is even (or) odd

num = int(input("Enter a number: "))

if num % 2 ==0 :
    print(f"{num}is even")
else:
    print(f"{num}is odd")


num = int(input("enter a number:"))
if num % 2 ==0:
    print(f"{num}is even")
elif num % 2 == 0 :
    print(f"{num}is odd")
else:
    print("Invalid input")    
          
# Program to check Pass or Fail

marks = int(input("Enter your marks: "))

if marks >= 40:   # condition for pass
    print(" You Passed!")
else:             # condition for fail
    print(" You Failed!")

 # Program to check temperature warning

temperature = float(input("Enter the temperature in °C: "))

if temperature > 40:
    print(" High Temperature Warning!.")
else:
    print(" Temperature is normal.")

#number divisible 

number = int(input("enter a number:"))

if number % 5 == 0:
    print("Divisible by 5")

#postive or negative     

number = int(input("enter a number:"))

if number >=0:
    print("positive")
else:
    print("negative")

#Greater 

number = int(input("enter a number:"))

if number > 100:
    print("number is greater than 100")
else:
    print("number is not greater than 100")

#Marks 
marks = int(input("enter marks:"))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("grade B")
elif marks >= 60:
    print("grade c")
elif marks >= 40:
    print("grade D")
else:
    print("fail")

#Largest 

a = int(input("enter first number: "))
b = int(input("enter second number:"))

if a > b:
    print("largest:",a)
elif b > a:
    print("largest:",b)
else:
    print("both are equal")
    
    
#largest of three numbers
a = int(input("enter first number: "))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if a >= b and a >= c:
    print("largest:",a)
elif b >= a and b >= c:
    print("largest:",b)
else:
    print("largest:",c)
    
    
#Days
day =int(input("enter day number: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")
    


#
a = float(input("enter first number: "))
b = float(input("enter second number: "))
operator = input("enter operator (+,-,*,/): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
    
    

#check username first
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "admin123":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")
    
    
#balance amount
balance = float(input("Enter balance:"))
amount = float(input("Enter withdrawl amount:"))

if amount >0:
    if amount <= balance:
        balance = balance - amount
        print("Withdrawl successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid amount")
    
    
#marks and attendance
marks = int(input("Enter marks: "))
attendance = float(input("Enter attendance percentage:"))

if marks >= 40:
    if attendance >= 75:
        print("Eligible")
    else:
        print("Not eligible due to attendance")
else:
    print("Fail")
    

#driving test 
age = int(input("Enter age:"))
test = input("Did you pass the driving test? (yes/no):")

if age >= 18:
    if test == "yes":
        print("License can be issued")
    else:
        print("pass the driving test first")
else:
    print("Not eligible due to age")
    
#bodmas 
print(2+13*2)

    