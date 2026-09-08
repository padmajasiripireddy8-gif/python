#logical operators
#and
age = 25
citizen = True
print(age >= 18 and citizen == True)

age = 16
citizen = True

print(age >= 18 and citizen == True)


#or
has_card = False
has_cash = True

print(has_card or has_cash)


#not
is_logged_in = True

print(not is_logged_in)


#atm eligibility checker

balance = 10000
withdraw = 5000  

print(withdraw > 0 and withdraw <= balance)


#student scholarship eligibility checker
marks = float(input("Enter marks: "))
attendance = float(input ("Enter attendance:"))

eligible = marks >= 85 and attendance >= 75
print("Scholarship Eligible:", eligible)


#identify operators
a = None

print(a is None)
print(a is not None)


#bitwise operators
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)


#electricity city bill calculator
units = int(input("Enter electricity units:"))

rate = 6

bill = units * rate

print("Electricity Bill:", bill)


#tavel expense calculator
travel = float(input("Travel expense: "))
food = float(input("Food expense: "))
hotel = float(input("Hotel expense: "))

total = travel + food + hotel

print("Total Expenses: ", total)