# exercise 2
# FAULTY CALCULATOR
""" DESIGN A CALCULATOR WHICH WILL CORRECTLY SOLVE ALL PROBLEM EXCEPT THE FOLLOWING
45 * 3 =555, 56+9 = 77 , 56/6 = 4
YOUR PROGRAM SHOULD TAKE OPERATOR AND THE TWO NUMBER AS INPUT FROM AND THEN RETURN THE RESULT """
print("hello welcome to faulty calculator\nPLEASE ENTER YOUR FIRST NUMBER :")
a = int(input())
print("PLEASE SECOND YOUR FIRST NUMBER :")
b = int(input())
print("PLEASE ASSIGN AN OPERATOR")
c=input()
if c =="+":
    if a ==56 and b==9:
        print("your sum is 77")
    else:
        print(" your sum is",a+b)
if c =="-":
    print("your substraction is",a-b)
if c =="*":
    if a ==45 and b==3:
        print("your multiplication is 555")
    else:
        print(" your multiplication is",a*b)
if c =="/":
    if a ==56 and b==6:
        print("your division is 4")
    else:
        print(" your division is",float(a/b))

print("thankyou for using us!")