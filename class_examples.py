
age_list = [21, 23, 23]

def print_ages(age_list): #def is for function
    for age in age_list: #age could be any variable 
        print(age) 


print_ages(age_list) #calling the function 


#ATM Example
balance = 100000
password = 1234 
attempts = 0
while attempts < 3: 
    enter_password = input("enter password: ")

    if enter_password == password:
        break 
    else:
        print("Incorrect password")
        attempts += 1 
if attempts == 3: 
    print("account locked") 
else: 
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        
        choice = input("Select option: ")
        
        if choice == "1":
            print("Balance:", balance)
        
        elif choice == "2":
            amount = float(input("Enter amount: "))
            balance -= amount
        
        elif choice == "3":
            amount = float(input("Enter amount: "))
            balance += amount
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid selection")



pin = "1233"
balance = 10000 
atmpt = 0 


while atmpt < 3:
    atmpt = input("Enter your pin: ") 
    break 
    atmpt += 1
if atmpt == 3: 
    print("incorrect pin, card temporarily blocked")







