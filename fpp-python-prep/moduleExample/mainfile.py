import MyModule.module2 as m2
#from MyModule.module2 import myfunction as myf

def myfunction():
    return "Mainfile: This is myfunction in the " + __name__ + " module."


if __name__ == "__main__": 
    print(m2.myfunction())
    #print(myf())
    print(myfunction())
else: 
    print ("Executed when imported")