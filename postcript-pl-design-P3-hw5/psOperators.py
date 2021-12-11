from colors import BLUE, CEND, CYAN, RED
from psItems import Value, ArrayValue, FunctionValue
'''
Boxiang Lin
'''
class Operators:
    def __init__(self, scoperule):
        #stack variables
        self.opstack = []  #assuming top of the stack is the end of the list
        self.dictstack = []  #assuming top of the stack is the end of the list
        self.scope = scoperule
        
        #The builtin operators supported by our interpreter
        self.builtin_operators = {
             #Arithmetic
             "add":self.add, "sub":self.sub, "mod":self.mod, "mul":self.mul,   
             
             #Comparision
             "eq":self.eq, "lt":self.lt, "gt":self.gt,
             
             #Array                      
             "length":self.length, "getinterval":self.getinterval, "putinterval":self.putinterval, "aload":self.aload, "astore":self.astore, 
             
             #Basic
             "dup":self.dup, "exch":self.exch, "pop":self.pop, "copy":self.copy, "clear":self.clear, "roll":self.roll, 
            #  "dict":self.psDict,  #no useful in SSPS
             "def":self.psDef,
            #  "begin":self.begin, #no useful in SSPS
            #  "end":self.end,  #no useful in SSPS
             "stack":self.stack, "count":self.count,
             
             "if":self.psIf, "ifelse":self.psIfelse, 'repeat':self.repeat, 'forall':self.forall
             
             
             # include the key value pairs where the keys are the PostScrip opertor names and the values are the function values that implement that operator. 
             # Make sure **not to call the functions** 
        }
    #-------  Operand Stack Operators --------------
    """
        Helper function. Pops the top value from opstack and returns it.
    """
    def opPop(self):
        return self.opstack.pop()

    """
       Helper function. Pushes the given value to the opstack.
    """
    def opPush(self,value):
        self.opstack.append(value)
        
    #------- Dict Stack Operators --------------
    
    """
       Helper function. Pops the top dictionary from dictstack and returns it.
    """   
    def dictPop(self):
        return self.dictstack.pop()

    """
       Helper function. Pushes the given dictionary onto the dictstack. 
    """   
    def dictPush(self, d):
        self.dictstack.append(d)

    """
       Helper function. Adds name:value pair to the top dictionary in the dictstack.
       (Note: If the dictstack is empty, first adds an empty dictionary to the dictstack then adds the name:value to that. 

       <NOTEs>: 
       name format start with "/" 
       value format is the integer
    """   
    def define(self,name, value):
        if len(self.dictstack) == 0:
            tup = (0, {})
            self.dictPush(tup)
        self.dictstack[-1][1][name] = value

    """
       Helper function. Searches the dictstack for a variable or function and returns its value. 
       (Starts searching at the top of the opstack; if name is not found returns None and prints an error message.
        Make sure to add '/' to the begining of the name.)
    """
    
    def search_static_dict(self, name):
        def dfs(idx):
            if name in self.dictstack[idx][1]:
                return self.dictstack[idx][1][name]
            # if (i, {...}) and i == index of stack, connor case link doesnt move anymore and not found such pair yet, return None
            elif self.dictstack[idx][0] == idx:
                return None
            else:
                return dfs(self.dictstack[idx][0])
        # return the value in a dict
        return dfs(len(self.dictstack) - 1)
    
    def lookup(self,name):
        the_name = '/' + name
        if self.scope == 'static':
            return self.search_static_dict(the_name)
        elif self.scope == 'dynamic':
            for tup in reversed(self.dictstack):
                if the_name in tup[1]:
                    return tup[1][the_name]
        print("Error LookUp: no such name in dictionary stack")
        return None
        
        
    #------- Arithmetic Operators --------------
    
    """
       Pops 2 values from opstack; checks if they are numerical (int); adds them; then pushes the result back to opstack. 
    """   
    def add(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op2 + op1)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: add expects 2 operands")
 
    """
       Pop 2 values from opstack; checks if they are numerical (int); subtracts them; and pushes the result back to opstack. 
    """   
    def sub(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op2 - op1)
            else:
                print("Error: sub - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1) 
        else:
            print("Error: sub expects 2 operands")

    """
        Pops 2 values from opstack; checks if they are numerical (int); multiplies them; and pushes the result back to opstack. 
    """    
    def mul(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op2 * op1)
            else:
                print("Error: mul - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1) 
        else:
            print("Error: mul expects 2 operands")

    """
        Pops 2 values from stack; checks if they are int values; calculates the remainder of dividing the bottom value by the top one; 
        pushes the result back to opstack.
    """ 
    def mod(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1, int) and isinstance(op2, int):
                self.opPush(op2 % op1)
            else:
                print("Error: mod - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1) 
        else:
            print("Error: mod expects 2 operands")
    #---------- Comparison Operators  -----------------
    """
       Pops the top two values from the opstack; pushes "True" is they are equal, otherwise pushes "False"
    """ 
    def eq(self):
        if len(self.opstack) > 1:
            x = self.opPop()
            y = self.opPop()
            if x == y:
                self.opPush(True)
            else:
                self.opPush(False)
        else:
            print("Error: - stack out of range" )

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is less than the top value, otherwise pushes "False"
    """ 
    def lt(self):
        if len(self.opstack) > 1:
            top = self.opPop()
            bottom = self.opPop()
            if bottom < top:
                self.opPush(True)
            else:
                self.opPush(False)
        else:
            print("Error: - stack out of range" )

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is greater than the top value, otherwise pushes "False"
    """ 
    def gt(self):
        if len(self.opstack) > 1:
            top = self.opPop()
            bottom = self.opPop()
            if bottom > top:
                self.opPush(True)
            else:
                self.opPush(False)
        else:
            print("Error: - stack out of range" )

    # ------- Array Operators --------------
    """ 
       Pops an array value from the operand opstack and calculates the length of it. Pushes the length back onto the opstack.
       The `length` method should support ArrayValue values.
    """
    def length(self):
        if isinstance(self.opstack[-1], ArrayValue):
            array = self.opPop().value
            self.opPush(len(array))
        else:
            print("Error: not a valid ArrayValue type")

    """ 
        Pops the `count` (int), an (zero-based) start `index`, and an array constant (ArrayValue) from the operand stack.  
        Pushes the slice of the array of length `count` starting at `index` onto the opstack.(i.e., from `index` to `index`+`count`) 
        If the end index of the slice goes beyond the array length, will give an error. 
    """
    def getinterval(self):
        count, start, array = self.opPop(), self.opPop(), self.opPop()
        # count inclusive of start index so -1
        if start >= 0 and start+count-1 < len(array.value) and isinstance(array, ArrayValue):
            interval = array.value[start: start+count]
            self.opPush(ArrayValue(interval))
        else:
            self.opPush(array)
            self.opPush(start)
            self.opPush(count)
            print("Error: out of range index occured or non ArrayValue type in the stack")

    """ 
        Pops an array constant (ArrayValue), start `index` (int), and another array constant (ArrayValue) from the operand stack.  
        Replaces the slice in the bottom ArrayValue starting at `index` with the top ArrayValue (the one we popped first). 
        The result is not pushed onto the stack.
        The index is 0-based. If the end index of the slice goes beyond the array length, will give an error. 
    """
    def putinterval(self):
        interval, start, array = self.opPop().value, self.opPop(), self.opPop().value
        # interval inclusive of start so -1
        if start + (len(interval) - 1) < len(array):
            array[start:start+len(interval)] = interval
        else:
            self.opPush(array)
            self.opPush(start)
            self.opPush(interval)
            print("Error: out of range index occured.")
            

    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pushes all values in the array constant to the opstack in order (the first value in the array should be pushed first). 
        Pushes the orginal array value back on to the stack. 
    """
    def aload(self):
        array = self.opPop().value
        for item in array:
            self.opPush(item)
        self.opPush(ArrayValue(array))
        
    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pops as many elements as the length of the array from the operand stack and stores them in the array constant. 
        The value which was on the top of the opstack will be the last element in the array. 
        Pushes the array value back onto the operand stack. 
    """
    def astore(self):
        array = self.opPop().value
        for i in range(len(array)):
            array[i] = self.opPop()
        array.reverse()
        self.opPush(ArrayValue(array))

    #------- Stack Manipulation and Print Operators --------------

    """
       This function implements the Postscript "pop operator". Calls self.opPop() to pop the top value from the opstack and discards the value. 
    """
    def pop (self):
        self.opPop()

    """
       Prints the opstack. The end of the list is the top of the stack. 
    """
    def stack(self):
        print(CYAN+'===**opstack**==='+CEND)
        for item in reversed(self.opstack):
            print(item)
        print(BLUE+'===**dictstack**==='+CEND)
        index_dict = len(self.dictstack) - 1
        for item in reversed(self.dictstack):
            print('----', index_dict, '----', item[0], '----')
            index_dict -= 1
            for k, v in item[1].items():
                print(k,"   ", v)
        print(RED+'================='+CEND)


    """
       Copies the top element in opstack.
    """
    def dup(self):
        if len(self.opstack) > 0:
            item = self.opstack[-1]
            self.opPush(item)
        else:
            print("Error: Stack is empty can't dup")

    """
       Pops an integer count from opstack, copies count number of values in the opstack. 
    """
    def copy(self):
        nums = self.opPop()
        if nums <= len(self.opstack):
            start_index = len(self.opstack) - nums 
            copy_item = self.opstack[start_index:]
            for item in copy_item:
                self.opPush(item)
        else:
            print("Error: the numbers of item copy out of range")


    """
        Counts the number of elements in the opstack and pushes the count onto the top of the opstack.
    """
    def count(self):
        c = len(self.opstack)
        self.opPush(c)

    """
       Clears the opstack.
    """
    def clear(self):
        self.opstack.clear()
        
    """
       swaps the top two elements in opstack
    """
    def exch(self):
        if len(self.opstack) > 1:
            top = self.opstack[-1]
            self.opstack[-1] = self.opstack[-2]
            self.opstack[-2] = top
        else:
            print("Error: - stack out of range" )

    """
        Implements roll operator.
        Pops two integer values (m, n) from opstack; 
        Rolls the top m values in opstack n times (if n is positive roll clockwise, otherwise roll counter-clockwise)
    """
    def roll(self):
        n, top_m = self.opPop(), self.opPop()
        length = len(self.opstack)
        if top_m <= length:
            start_index = length - top_m  
            sublist = self.opstack[start_index:]
            if n < 0: 
                for i in range(n,0):
                    sublist = sublist[1:] + sublist[:1]
            else:
                for i in range(n):
                    sublist = sublist[-1:] + sublist[:-1]
            self.opstack[start_index:] = sublist
        else:
            print("Error: the numbers of item to ratate out of range")

    """
       Pops an integer from the opstack (size argument) and pushes an  empty dictionary onto the opstack.
    """
    def psDict(self):
        if isinstance(self.opstack[-1], int):
            self.opPop()
            self.opPush({})
        else:
            print("Error: the top of the stack is not int, can't be the intial size." ) 

    """
       Pops the dictionary at the top of the opstack; pushes it to the dictstack.
    """
    def begin(self):
        if isinstance(self.opstack[-1], dict):
            self.dictPush(self.opPop())
        else:
            print("Error: the top of the stack is not a dictionary")

    """
       Removes the top dictionary from dictstack.
    """
    def end(self):
        self.dictPop()
        
    """
       Pops a name and a value from opstack, adds the name:value pair to the top dictionary by calling define.  
    """
    def psDef(self):
        if len(self.opstack) > 1:
            value = self.opPop()
            name = self.opPop()
            self.define(name, value)
        else:
            print("Error: stack out of range exception")


    # ------- if/ifelse Operators --------------
    """
       Implements if operator. 
       Pops the `ifbody` and the `condition` from opstack. 
       If the condition is True, evaluates the `ifbody`.  
    """
    def psIf(self):
        body = self.opPop()
        condition = self.opPop()
        if condition and isinstance(body, FunctionValue):
            body.apply(self, len(self.dictstack)-1)

    """
       Implements ifelse operator. 
       Pops the `elsebody`, `ifbody`, and the condition from opstack. 
       If the condition is True, evaluate `ifbody`, otherwise evaluate `elsebody`. 
    """
    def psIfelse(self):
        body2, body1, condition = self.opPop(), self.opPop(), self.opPop()
        if condition:
            body1.apply(self, len(self.dictstack)-1)
        elif not condition:
            body2.apply(self, len(self.dictstack)-1)
        else:
            print("need code array to perform computation")


    #------- Loop Operators --------------
    """
       Implements repeat operator.   
       Pops the `loop_body` (FunctionValue) and loop `count` (int) arguments from opstack; 
       Evaluates (applies) the `loopbody` `count` times. 
       Will be completed in part-2. 
    """  
    def repeat(self):
        body, count = self.opPop(), self.opPop()
        for i in range(count):
            body.apply(self, len(self.dictstack)-1)
     
    """
       Implements forall operator.   
       Pops a `codearray` (FunctionValue) and an `array` (ArrayValue) from opstack; 
       Evaluates (applies) the `codearray` on every value in the `array`.  
       Will be completed in part-2. 
    """ 
    def forall(self):
        body = self.opPop()
        arr = self.opPop().value
        for item in arr:
            self.opPush(item)
            body.apply(self, len(self.dictstack)-1)

    #--- used in the setup of unittests 
    def clearBoth(self):
        self.opstack[:] = []
        self.dictstack[:] = []
    
    def cleanTop(self):
        if len(self.opstack)>1:
            if self.opstack[-1] is None:
                self.opstack.pop()
