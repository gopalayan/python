import numpy as np
a=np.zeros((2,2))
b=np.zeros((2,2))
c=np.zeros((2,2))
a1=int(input("enter yr d"))
for i in range(0,2):
    for j in  range(0,2):
        a[i][j]=int(input("enter ur element "))
for i in range(0,2):
    for j in  range(0,2):
        b[i][j]=int(input("enter ur element "))
for i in range(0,2):
    for j in  range(0,2):
        for k in range(0,2):
           c[i][j]=a[i][k]*b[k][j]+c[i][j]

print(a)   
print(b)
print(c)             