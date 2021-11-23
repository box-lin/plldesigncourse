debugging = True
def debug(*s): 
    if debugging: 
        print(*s)

#Example use of iterators

def getCourse(it):
    course = []
    for c in it:
        if c=='-':
            return course
        else:
            course.append(c)
    return course

i = iter("CptS355-CptS322-CptS321")
course1 = getCourse(i)
course2 = getCourse(i)
course3 = getCourse(i)

debug(''.join(course1))
debug(''.join(course2))
debug(''.join(course3))
debug("--------------------------------------------------------")


# Additional Iterator Examples

"""Generates an infinite sequence of natural numbers"""
class Naturals(object):
    def __init__(self,init):
        self.current = init
    def __next__(self):
        result = self.current
        self.current += 1
        return result
    def __iter__(self):
        return self

#-------------------------------------------------------------

"""Generates an  sequence of natural numbers from init to N (inclusive)"""
class NaturalsUptoN(object):
    def __init__(self,init,N):
        self.current = init
        self.N = N
    def __next__(self):
        if self.current > self.N: 
            raise StopIteration
        result = self.current
        self.current += 1
        return result
    def __iter__(self):
        return self

#-------------------------------------------------------------

"""Create a copy of the input iterator sequence"""
class copyIter(object):
    def __init__(self,it):
        self.input = it
        self.current = self._getNextInput()

    def _getNextInput(self):
        try:
            curr = next(self.input)
        except:
            curr = None
        return curr

    def __next__(self):
        if self.current is None:
            raise StopIteration
        result = self.current
        self.current = self._getNextInput()
        return result

    def __iter__(self):
        return self

it = copyIter(iter([1,2,3,4,5,6]))
debug("First:", it.__next__())
debug("Second", it.__next__())
for item in it:
    debug(item)
    if item == 5:
        break
debug("last:",it.__next__()) # print 6
#debug(it.__next__()) # raise the StopIteration exception
debug("--------------------------------------------------------")
#-------------------------------------------------------------
"""
Generate an iterator which takes an iterator of strings and generates a sequence of strings 
where each string is the concatanation of consecutive strings from the input iterator. 
Example : concatConsecutive(iter(["CptS","355","CptS","322","done"]))
          should return "CptS355", "CptS322", "done" 
"""
class concatConsecutive(object):
    def __init__(self,it,n):
        self.input = it
        self.current = self._getNextInput()
        self.n = n

    def _getNextInput(self):
        try:
            current = next(self.input)
        except:
            current = None
        return current

    def __next__(self):
        localN = self.n
        if self.current is None:
            raise StopIteration
        word = self.current 
        self.current = self._getNextInput()   
        while localN>0:    
            localN = localN-1
            if self.current is None:
                break
            else:    
                word += self.current
                self.current = self._getNextInput() 
                if localN==1:
                    break
        return word   

    def __iter__(self):
        return self

it = concatConsecutive(iter(["CptS","355","*","CptS","322","*","***","done"]),3)
for s in it:
    debug("Next string: ", s)

debug("--------------------------------------------------------")

# #-------------------------------------------------------------
"""generator example"""
def letters(start, finish):
   current = start
   while current <= finish:
       debug("before yield")
       yield current
       debug("after yield")
       current = chr(ord(current)+1)


gLetters = letters("a","d")
debug(gLetters.__next__())

for a in gLetters:
    debug(a)
list(gLetters)


