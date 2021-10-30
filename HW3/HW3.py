# CptS 355 - Fall 2021 - Assignment 3
# Boxiang Lin

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

my_cats_log =  {(2,2019):{"Oceanfish":7, "Tuna":1, "Whitefish":3, "Chicken":4, "Beef":2},
                (5,2019):{"Oceanfish":6, "Tuna":2, "Whitefish":1, "Salmon":3, "Chicken":6},
                (9,2019):{"Tuna":3, "Whitefish":3, "Salmon":2, "Chicken":5, "Beef":2, "Turkey":1, "Sardines":1},
                (5,2020):{"Whitefish":5, "Sardines":3, "Chicken":7, "Beef":3},
                (8,2020):{"Oceanfish":3, "Tuna":2, "Whitefish":2, "Salmon":2, "Chicken":4, "Beef":2, "Turkey":1},
                (10,2020):{"Tuna":2, "Whitefish":2, "Salmon":2, "Chicken":4, "Beef":2, "Turkey":4, "Sardines":1},
                (12,2020):{"Chicken":7,"Beef":3, "Turkey":4, "Whitefish":1, "Sardines":2},
                (4,2021):{"Salmon":2,"Whitefish":4, "Turkey":2, "Beef":4, "Tuna":3, "MixedGrill": 2}, 
                (5,2021):{"Tuna":5,"Beef":4, "Scallop":4, "Chicken":3}, 
                (6,2021):{"Turkey":2,"Salmon":2, "Scallop":5, "Oceanfish":5, "Sardines":3}, 
                (9,2021):{"Chicken":8,"Beef":6},                 
                (10,2021):{ "Sardines":1, "Tuna":2, "Whitefish":2, "Salmon":2, "Chicken":4, "Beef":2, "Turkey":4} }

p1a_output = {2019: {'Oceanfish': 13, 'Tuna': 6, 'Whitefish': 7, 'Chicken': 15, 'Beef': 4, 'Salmon': 5, 'Turkey': 1, 'Sardines': 1}, 
              2020: {'Whitefish': 10, 'Sardines': 6, 'Chicken': 22, 'Beef': 10, 'Oceanfish': 3, 'Tuna': 4, 'Salmon': 4, 'Turkey': 9}, 
              2021: {'Salmon': 6, 'Whitefish': 6, 'Turkey': 8, 'Beef': 16, 'Tuna': 10, 'MixedGrill': 2, 'Scallop': 9, 'Chicken': 15, 'Oceanfish': 5, 'Sardines': 4}}


## problem 1(a) merge_by_year - 10%
def merge_by_year(my_cats_log): 
     res = {} 
     for k,v in my_cats_log.items():
          if k[1] not in res.keys(): res[k[1]] = {} #if such year not in res key intialize res[year] = {}
          for fish, val in v.items():
               if fish not in res[k[1]].keys():  #if such fish not in {}.key intialize res[year][fish] = val
                    res[k[1]][fish] = val
               else:                             #otherwise such fish in {fish: preval} then make it {fish:  preval + curval}
                    res[k[1]][fish] += val
     return res

from functools import reduce

## problem 1(b) merge_year - 15%
def merge_year(my_cats_log, year):
     year_table = list(filter(lambda x: x[0][1] == year, my_cats_log.items())) # filter the dictionaties with second element in tuple key is year
     year_val = list(map(lambda x: x[1], year_table))  # get rid of tuble key
     def combine_dics(d1, d2):
          common_items = map(lambda x: (x[0], x[1] + d2.get(x[0], 0)), d1.items() ) 
          other_items = filter(lambda t: t[0] not in d1.keys(), d2.items()) # item not comman and only from d2
          return list(common_items) + list(other_items)
     res = dict(reduce(lambda d1, d2: combine_dics(dict(d1),dict(d2)), year_val))
     return res

# problem 1(c) getmax_of_flavor - 15%
def getmax_of_flavor(my_cats_log, flavor):
     candidate = filter(lambda x: flavor in x[1], my_cats_log.items()) # candidate contains flavor
     def compare(l1, l2):  # candidate with higher flavor value get selected
          v1 = l1[1][flavor]
          v2 = l2[1][flavor]
          return l1 if v1 > v2 else l2
     max_candidate = reduce(lambda x, y: compare(x,y), candidate)  #bubbling toward the good candidates eventually left candidate with max flavor value
     res = (max_candidate[0],max_candidate[1][flavor]) # setup tuple
     return res 

graph = {'A':{'B','C','D'},'B':{'C'},'C':{'B','E','F','G'},'D':{'A','E','F'},'E':{'F'}, 'F':{'E', 'G'},'G':{}, 'H':{'F','G'}}

## problem 2(a) follow_the_follower - 10%
def follow_the_follower(graph):
     res = []
     for k,v in graph.items(): 
          for edge in v:
               if edge in graph.keys(): 
                    if k in graph[edge]: 
                         res.append((k, edge))
     return res

## problem 2(b) follow_the_follower2 - 6%
def follow_the_follower2(graph):
     return [(k,edges) for k,v in graph.items() for edges in v if edges in graph.keys() if k in graph[edges]]

## problem 3 - connected - 15%
def connected (graph, node1, node2):
     res = [False] # for reference flag
     visited = set()
     def dfs(cur_e, target_e):
          if cur_e == target_e:  # if the current node equal to target
               res[0] = True     # flag it true and stop
               return
          visited.add(cur_e)     # every current node add to a set for visit history check
          if cur_e in graph:     # if the cur node in graph, check its edges
               for e in graph[cur_e]: # we will have to go through all node in curnode edges
                    if e in visited: continue   # if it is the node that we previsou visited, visit its next node.
                    dfs(e, target_e)     # dfs to a node.
          else:
               return # else a node not in a graph, we stop and backtrack check.
     dfs(node1, node2)
     return res[0]


## problem 4(a) - lazy_word_reader - 20%
#required Iterator class
'''
Read the txt line per line
Each line gets to check whether is /n(blank line) or ""(end of the file)
If is /n keep readline until a valid line.
If is end of file "" raise stopIteration.
If is a valid line split it and turn it into a iterator.
          --> then return each word from a line iterator
          --> line iterator update when catch occur (return word being None)
'''
class lazy_word_reader():

     def __init__(self, filename):
          self.fn = open(filename, 'r')
          self.line_it = self._getNextLine() 
 
     # check to see if end of it iterator
     def _getNextLine(self):
          line = self.fn.readline()
          # when next line is empty loop it.
          while line == '\n':
               line = self.fn.readline()

          if line == "":
               self.fn.close()
               raise StopIteration
          else:
               return iter(line.split())

     def _getword(self):
          try:
               w = self.line_it.__next__()
          except:
               w = None
          return w

     #def _getWord(self):
     def __next__(self):
          word = self._getword() # get the word from the line iterator
          if word == None:
               self.line_it = self._getNextLine() #if end of the line, will raise stop at _getNextLine
               word = self._getword()
          return word

     def __iter__(self):
          return self


# problem 4(b) - word_histogram - 3%
def word_histogram(words):
     memo = {}
     for w in words:
          if w in memo:
               memo[w] += 1
          else:
               memo[w] = 1
     res = list(memo.items())
     return sorted(sorted(res), key = lambda x: x[1], reverse=True)
