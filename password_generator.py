import random
import string
print("\t\t\t------((welcome to Password Generator))-------")
print()
size=int(input("Enter the size of your password:"))
print()
upperc=string.ascii_uppercase
lowerc=string.ascii_lowercase
symbols=string.punctuation
num=string.digits
com=upperc+lowerc+symbols+num
a=random.sample(com,size)
password="".join(a)
print("Your New Password is: ",password)
print("\t\t\t~~~~Thank You for Visiting~~~~")