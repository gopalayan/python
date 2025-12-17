numbers=[1,2,3,4,5]
total=0
for num in numbers:
    total+=num
print("sum",total)

number=[1,2,3,4,5]
maximum=number[0]
minimum=number[0]
for num in number:
    if num>maximum:
        maximum=num
    if num<minimum:
        minimum=num

print(maximum)    
print(minimum)