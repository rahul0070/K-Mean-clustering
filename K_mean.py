from random import randint
l=[]

def nearest(c1, c2):
    #print("Entering nearest function.")
    if(c1>=c2):
        return (c1-c2)
    else:
        return (c2-c1)

def avg(list):
    #print("Entering average function.")
    sum=0
    for i in range((len(list))):
        sum=sum+list[i]
    return (sum/len(list))

def k_mean(a, b):
    #print("Entering K mean function.")
    l1=[]
    l2=[]
    for i in range((len(l))):
        n1=nearest(l[i], a)
        n2=nearest(l[i], b)
        if(n1>n2):
            l1.append(l[i])
        elif(n2>=n1):
            l2.append(l[i])
    a1=avg(l1)
    a2=avg(l2)
    if a1==b and a2==a:
        print("Group 1:")
        print(l1)
        print("Group 2:")
        print(l2)
        ex=input("Program executed.")
    else:
        #print("Recursion.")
        k_mean(a1, a2)



#main
while True:
    x=input("Enter the list of numbers:")
    if (x!="end"):
        l.append(x)
    else:
        break

for f in range(len(l)):
    l[f]=int(l[f])

lenght=len(l)-1
while True:
    #print("Finding rand int.")
    r1=randint(0, lenght)
    r2=randint(0, lenght)
    if(r1!=r2):
        k_mean(l[r1], l[r2])
        break

