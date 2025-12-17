def div(x,y):
    try: 
        print(x/y)
    except ZeroDivisionError as er:

        print("not divide..")
div(10,0)