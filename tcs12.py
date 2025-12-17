n=int(input("enter ur hr:"))
re=0
g=list()
entry=list(map(int,input("enter ur entry list:").split()))
exit=list(map(int,input("enter ur exit list:").split()))
for i in range(n):
    re=entry[i]-exit[i]+re
    g.append(re)  
print(max(g))   
    