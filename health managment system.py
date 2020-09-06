# Health management system
import datetime
# Firstly we have to ask him to save the name or we can preset for it
import datetime
def gettime():
    return datetime.datetime.now()
name1 = int(input(" Hey, welcome to stay fit management dice.\n"
                  " Please enter 1 for sumit.\n "
                  "Please enter 2 for kunal.\n "
                  "Please enter 3 for kartik.\n"))
if name1 == 1:
    s1 = int(input("Hey Sumit!, welcome back.\n If you wanna update your Exercise choose 1.\n"
                  " If you wanna update your diet choose 2. \n"))
    if s1 == 1:
        value = input("type here\n")
        with open("sumit_ex.txt", "a") as op:
            op.write(str([str(gettime())]) + ": " + value + "\n")
        print("successfully written")
    elif s1==2:
        value = input("type here\n")
        with open("sumit_food.txt", "a") as op:
            op.write(str([str(gettime())]) + ": " + value + "\n")
        print("successfully written")
elif name1== 2:
    s1 = int(input("Hey "
                   "kunal!, welcome back.\n If you wanna update your Exercise choose 1.\n"
                   " If you wanna update your diet choose 2. \n"))
    if s1 == 1:
        value = input("type here\n")
        with open("kunal_ex.txt", "a") as op:
            op.write(str([str(gettime())]) + ": " + value + "\n")
        print("successfully written")
    elif s1 == 2:
        value = input("type here\n")
        with open("kunal_food.txt", "a") as op:
            op.write(str([str(gettime())]) + ": " + value + "\n")
        print("successfully written")
elif name1==3:
    s1 = int(input("Hey kartik!, welcome back.\n If you wanna update your Exercise choose 1.\n"
                   " If you wanna update your diet choose 2. \n"))
    if s1 == 1:
        value = input("type here\n")
        with open("kartik_ex.txt", "a") as op:
            op.write(str([str(gettime())]) + ": " + value + "\n")
        print("successfully written")
    elif s1 == 2:
        value = input("type here\n")
        with open("kartik_food.txt", "a") as op:
            op.write(str([str(gettime())]) + ": " + value + "\n")
        print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
    def retrieve(k):
        if k==1:
            c=int(input("enter 1 for excercise and 2 for food"))
            if(c==1):
                with open("sumit_ex.txt") as op:
                    for i in op:
                        print(i,end="")
        elif(c==2):
            with open("sumit_food.txt.txt") as op:
                for i in op:
                    print(i, end="")
        elif(k==2):
            c = int(input("enter 1 for excercise and 2 for food"))
            if (c == 1):
                with open("kunal_ex.txt") as op:
                    for i in op:
                        print(i, end="")
        elif (c == 2):
            with open("kunal_food.txt") as op:
                for i in op:
                    print(i, end="")
        elif(k==3):
            c = int(input("enter 1 for excersise and 2 for food"))
            if (c == 1):
                with open("kartik_ex.txt") as op:
                    for i in op:
                        print(i, end="")
        elif (c == 2):
            with open("kartik_food.txt") as op:
                for i in op:
                    print(i, end="")
else:
     print("plz enter valid input (harry,rohan,hammad)")
     print("health management system: ")
a=int(input("press 1 for lock the value and 2 for retrieve "))

if a==1:
    a = int(input("press 1 for sumit 2 for kunal 3 for kartik "))
    take(b)
else:
    b = int(input("press 1 for sumit 2 for kunal 3 for kartik"))
    retrieve(b)







