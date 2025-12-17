n=int(input("enter ur no:"))
count=0
avarage=0
for i in range(n):
    name=input("enter ur name:")
    age=int(input("enter ur age:"))
    grade=input("enter ur grade:")
    gender=input("enter the gender:")
    if(gender=="female"):
        count=count+1
        if(age>=20):
            avarage=ord(grade)+avarage
print(avarage//count)
