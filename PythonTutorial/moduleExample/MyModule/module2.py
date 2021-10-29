import MyModule.module1 as m1

x =  10 

def myfunction():
    return "Module2 : This is myfunction in the " + __name__ + " module."


if __name__ == "__main__": 
    print ("Module 2: Executed when invoked directly")
    print(m1.myfunction())
    print(myfunction())
else: 
    print ("Executed when imported")