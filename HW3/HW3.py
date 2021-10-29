# CptS 355 - Fall 2021 - Assignment 3
# Please include your name and the names of the students with whom you discussed any of the problems in this homework

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
# def merge_year(my_cats_log, year):
#      year_table = list(filter(lambda x: x[0][1] == year, my_cats_log.items()))
#      year_val = list(map(lambda x: x[1], year_table))


#      #common_items = map (lambda x : (x[0], x[1]+ ))
#      print(year_val)

# merge_year(my_cats_log,2019)
# merge_year(my_cats_log, 2019)

## problem 1(c) getmax_of_flavor - 15%
# def getmax_of_flavor(my_cats_log, flavor):
#      flavor_table = (lambda x: x[flavor] if flavor in x else None, my_cats_log.values())
#      print(list(flavor_table))

graph = {'A':{'B','C','D'},'B':{'C'},'C':{'B','E','F','G'},'D':{'A','E','F'},'E':{'F'}, 'F':{'E', 'G'},'G':{}, 'H':{'F','G'}}

## problem 2(a) follow_the_follower - 10%
def follow_the_follower(graph):
     res = []
     for k,v in graph.items(): 
          for edges in v:
               if k in graph[edges]: res.append((k, edges))
     return res

## problem 2(b) follow_the_follower2 - 6%
def follow_the_follower2(graph):
     return [(k,edges) for k,v in graph.items() for edges in v if k in graph[edges]]

## problem 3 - connected - 15%
# def connected (graph, node1, node2):
#      res = [False] # for reference flag
#      visited = set()
#      def dfs(cur_e, target_e):
#           print(cur_e)
#           if cur_e == target_e:  # if the current node equal to target
#                res[0] = True     # flag it true and stop
#                return
#           visited.add(cur_e)     # every current node add to a set for visit history check
#           if cur_e in graph:     # if the cur node in graph, check its edges
#                for e in graph[cur_e]: # we will have to go through all node in curnode edges
#                     if e in visited: continue   # if it is the node that we previsou visited, visit its next node.
#                     dfs(e, target_e)     # dfs to a node.
#           else:
#                return # else a node not in a graph, we stop and backtrack check.
#      dfs(node1, node2)
#      return res[0]
def connected (graph, node1, node2):
     res = [False] # for reference flag
     visited = set()
     visited.add(node1)
     def dfs(edges, target_e):
          if target_e in edges:
               res[0] = True    
               return
          for e in edges: 
               if e in visited: continue 
               visited.add(e) 
               if e not in graph: return
               else: dfs(graph[e], target_e)
     dfs(graph[node1], node2)
     return res[0]


## problem 4(a) - lazy_word_reader - 20%
#required Iterator class
f = open('testfile.txt', 'r')
line = f.readline()
print(line)

class lazy_word_reader():
     def __init__()


## problem 4(b) - word_histogram - 3%
