#program for simple calculator

#funtion to add two nums
def add(a,b):
    return a+b

#funtion to subtract two nums
def sub(a,b):
    return a-b

#funtion to divide two nums
def div(a,b):
    return a/b

#funtion to modulus two nums
def mod(a,b):
    return a%b

#funtion to multiply two nums
def mul(a,b):
    return a*b
#giving options
print("select an option")
print()
print("1.Addition\n2.Subraction\n3.Division\n4.Modulus\n5.Multiplication")
print()

while True :
    #asking reader's choice
    choice=input("Select a Choice [1,2,3,4,5] ")
    print()
    if (choice in ('1','2','3','4','5')):
        
        #reading two numbers
        a=float(input("enter first number "))
        b=float(input("enter second number "))
        print()
        
        #addition
        if choice=='1':
            print(f'{a} + {b} = ',add(a,b))
            print()
            
        #subtration
        elif choice=='2':
            print(f'{a} - {b} = ',sub(a,b))
            print()
            
        #division
        elif choice=='3':
            print(f'{a} / {b} = ',div(a,b))
            print()

        #modulus
        elif choice=='4':
            print(f'{a} % {b} = ',mod(a,b))
            print()

        #multiplication
        elif choice=='5':
            print(f'{a} * {b} = ',mul(a,b))
            print()
            
        #asking user to continue or stop
            
        print("Do you want to continue?")
        next_choice=input("yes or No ").lower()
        print()
        if next_choice=="no":
            print("Thank You! ")
            break
        
    #if choice not in range(1,6)  
    else:
        print("Select a valid Choice ")
        print()
        
    

    
