l=[4,5,8,1,2]
def filter_func(a):
    return a>3
nwl=list(filter(filter_func,l))
print(nwl)
