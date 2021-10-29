# CptS 355 - Fall 2021 - Lab 3
# Boxiang Lin

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

## problem 1 getNumCases 
def getNumCases(data, counties, months):
     res = 0
     for k,v in data.items():
          if k in counties:
               for key, val in v.items():
                    if key in months:
                         res += val
     return res

## problem 2 getMonthlyCases
def getMonthlyCases(data):
     res = {}
     counties = list(data.keys()) # Get all counties in a list
     for v in data.values(): 
          for month in v.keys():
               temp = {} # a temp dict to store {county:value, ....} after all counties processed we want it to be empty for the next round.
               for c in counties: 
                    if month in data[c]: # there might be month not in a county we will exclude it.
                         temp[c] = data[c][month]  # if a month is in a county, we get its value from data dict 
               res[month] = temp 
          # not break here because each county has different range of months, we will brute force through them.
     return res


from functools import reduce
from typing import Iterable

## problem 3 mostCases 
def mostCases(data):
     d = getMonthlyCases(data) #data that retreive from q2
     # Using map to first get rid of months key then map again to get rid of counties key --> left with only integer values, then apply reduce
     # to sum them up and pair with month as a tuple.
     m_of_val = list(map(lambda x: (x,  reduce(lambda i,j: i+j, list(map(lambda y: d[x][y], d[x])) )  ), d)) #list of tuples (month, sum_val)
     return reduce(lambda x,y : x if x[1] > y[1] else y, m_of_val) #bubble up the max

## problem 4a) searchDicts(L,k)
def searchDicts(L,k):
     for i in range (len(L)-1, -1, -1):
          if k in L[i].keys():
               return L[i][k]
     return None

## problem 4b) searchDicts2(L,k)
def searchDicts2(L,K):
     def helper(i, L, K):
          if not L: return None  # when K not in L, we will keep delete until empty L
          if K in L[i][1].keys(): return L[i][1][K] 
          flag = i  # record current i to flag
          i = L[i][0]
          L.remove(L[flag]) # Since we visited this sublist and not found the equivalent k, delete it, this way we can better manage our base case.
          return helper(i, L, K)
     return helper(len(L) -1 , L, K)


## problem 5 - getLongest
def getLongest(L):
     res = [""] # referencing the max string at index 0.
     def helper(L):
          if L == []: return # slicing list eventually get to [], we stop.

          if isinstance(L[0], str): #if the first index of element is str we compare the length
               if len(L[0]) > len(res[0]): 
                    res[0] = L[0]
          elif isinstance(L[0], list):  #otherwise could be a list, we recursively go through.
               helper(L[0]) 

          helper(L[1:]) #in case there is L - L[0] or L[0] - L[0][0] or.....  remains we recursively went through and perform above checks.
     helper(L)
     return res[0]


## problem 6 - apply2nextN 
class apply2nextN:
     def __init__(self, f, n, it):
          self.n = n 
          self.f = f
          self.input= it
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
          local_n = self.n
          res = self.current
          self.current = self._getNextInput()
          while local_n > 1: 
               local_n -= 1
               if self.current is None:
                    break
               res = self.f(res, self.current)
               self.current = self._getNextInput()
          return res
     
     def __iter__(self):
          return self

          
