print("\t\t---Calculate Your Numbers Here---\t\t")
print()
while True:
    print()
    print("+ for Addition, - for Subtraction, * for Multiplication, / for Division, e for Exit")
    n1=float(input("Enter your first number: "))
    n2=float(input("Enter your second number: "))
    op=input("Enter your choice(+,-,*,/,e): ")
    if op=='e':
        print("Thank you for using my calculator")
        break
    if op=='+':
        print(n1 ,"+", n2)
        print("The Result is: ",n1+n2)
    elif op=='-':
        print(n1 ,"-", n2)
        print("The Result is: ",n1-n2)
    elif op=='*':
        print(n1 ,"*", n2)
        print("The Result is: ",n1*n2)
    elif op=='/':
        print(n1 ,"/", n2)
        print("The Result is: ",n1/n2)
    else:
        print("Wrong Input\n Try again")