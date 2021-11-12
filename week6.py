ans= "yes"

while ans== "yes":
    ans=input("do you want to go again? ")
count=1
while count <10:
    count+=2
    print (count)

        
import random

num1= random.randint(0,10)
num2=random.randint(0,10)

answer= eval(input("what is", num1, "plus", num2 ))

while answer!=num1+num2:
    answer= eval(input("what is", num1, "plus", num2))

print ("correct")


L1= [1,2,3,4,5]
L2= [1,2,3,4,5]

for L1 in range (1,6):
    for L2 in range (1,6):
        print (L1, "by", L2, "=", L1*L2)

countt= 10
while countt >0:
    countt -=1
    if countt == 6:
        continue
    if countt == 1:
        break
    print (countt)
