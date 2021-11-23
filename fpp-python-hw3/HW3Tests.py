import unittest
from HW3 import *
## Boxiang Lin
class HW3SampleTests(unittest.TestCase):
    "Unittest setup file. Unitetst framework will run this before every test."
    def setUp(self):
        self.my_cats_log =  {(2,2019):{"Oceanfish":7, "Tuna":1, "Whitefish":3, "Chicken":4, "Beef":2},
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
            (10,2021):{ "Sardines":1, "Tuna":2, "Whitefish":2, "Salmon":2, "Chicken":4, "Beef":2, "Turkey":4}
        }
        self.graph = {'A':{'B','C','D'},'B':{'C'},'C':{'B','E','F','G'},'D':{'A','E','F'},'E':{'F'}, 'F':{'E', 'G'},'G':{}, 'H':{'F','G'}}

        #################################################### Test Data ##################################################################
        self.random_log = {
            (1,2018): {'A':2, 'B': 12, 'C': 21, 'D': 1, 'E':9},
            (5,2018): {'B': 10, 'C': 11, 'D': 2, 'E':7, 'F': 11},
            (8,2018): {'A': 10, 'B': 1, 'E': 2, 'F': 20},
            (11,2019): {'A':1, 'B': 2, 'C': 20, 'D': 3, 'E':2},
            (12,2020): {'C':9, 'D': 1, 'F': 20},
            (10,2020): {'A':1, 'B': 222, 'C': 2, 'D': 333, 'E':12}
        }

        self.mygraph = {'A': {'B', 'C', 'D'}, 'B': {'A', 'E', 'F'}, 'E': {'C'}, 'C':{'H', 'E'},'D':{}, 'F':{'E'}}
        #################################################################################################################################
    
    #--- Problem 1(a)----------------------------------
    def test_1_merge_by_year(self):
        output = {2019: {'Oceanfish': 13, 'Tuna': 6, 'Whitefish': 7, 'Chicken': 15, 'Beef': 4, 'Salmon': 5, 'Turkey': 1, 'Sardines': 1}, 
                  2020: {'Whitefish': 10, 'Sardines': 6, 'Chicken': 22, 'Beef': 10, 'Oceanfish': 3, 'Tuna': 4, 'Salmon': 4, 'Turkey': 9}, 
                  2021: {'Salmon': 6, 'Whitefish': 6, 'Turkey': 8, 'Beef': 16, 'Tuna': 10, 'MixedGrill': 2, 'Scallop': 9, 'Chicken': 15, 'Oceanfish': 5, 'Sardines': 4}}
        self.assertDictEqual(merge_by_year(self.my_cats_log),output)


    # Additional 1(a)
    def test_2_merge_by_year(self):
        output = {
            2018: {'A': 12, 'B': 23, 'C': 32, 'D': 3, 'E': 18, 'F': 31},
            2019: {'A': 1, 'B': 2, 'C': 20, 'D': 3, 'E': 2},
            2020: {'A': 1, 'B': 222, 'C': 11, 'D': 334, 'F': 20,'E': 12}
        }
        self.assertDictEqual(merge_by_year(self.random_log),output)
    
    #--- Problem 1(b)----------------------------------
    def test_1_merge_year(self):
        output1 = {'Oceanfish': 13, 'Tuna': 6, 'Whitefish': 7, 'Chicken': 15, 'Beef': 4, 'Salmon': 5, 'Turkey': 1, 'Sardines': 1}
        self.assertDictEqual(merge_year(self.my_cats_log,2019),output1 )
        output2 = {'Salmon': 6, 'Whitefish': 6, 'Turkey': 8, 'Beef': 16, 'Tuna': 10, 'MixedGrill': 2, 'Scallop': 9, 'Chicken': 15, 'Oceanfish': 5, 'Sardines': 4}
        self.assertDictEqual(merge_year(self.my_cats_log,2021),output2 )

    # Addtional 1(b)
    def test_2_merge_year(self):
        output1 = {'A': 12, 'B': 23, 'C': 32, 'D': 3, 'E': 18, 'F': 31}
        output2 = {'A': 1, 'B': 222, 'C': 11, 'D': 334, 'F': 20,'E': 12}
        self.assertDictEqual(merge_year(self.random_log,2018),output1 )
        self.assertDictEqual(merge_year(self.random_log,2020),output2 )

    #--- Problem 1(c)----------------------------------
    def test_1_getmax_of_flavor(self):
        output1 = ((5, 2021), 5)
        self.assertTupleEqual(getmax_of_flavor(self.my_cats_log,"Tuna"),output1 )
        output2 = ((9, 2021), 6)
        self.assertTupleEqual(getmax_of_flavor(self.my_cats_log,"Beef"),output2 )

    # Additional 1(c)
    def test_2_getmax_of_flavor(self):
        output1 = ((10, 2020), 333)
        self.assertTupleEqual(getmax_of_flavor(self.random_log,'D'),output1 )
        output2 = ((1,2018), 21)
        self.assertTupleEqual(getmax_of_flavor(self.random_log,'C'),output2 )

    #--- Problem 2(a)----------------------------------
    def test_1_follow_the_follower(self):
        output = [('A', 'D'), ('B', 'C'), ('C', 'B'), ('D', 'A'), ('E', 'F'), ('F', 'E')]
        self.assertListEqual(follow_the_follower(self.graph),output )

    # Additional 2(a)
    def test_2_follow_the_follower(self):
        output = [('A', 'B'), ('B', 'A'), ('E', 'C'), ('C', 'E')] 
        self.assertListEqual(follow_the_follower(self.mygraph),output ) 
    
    #--- Problem 2(b)----------------------------------
    def test_1_follow_the_follower2(self):
        output = [('A', 'D'), ('B', 'C'), ('C', 'B'), ('D', 'A'), ('E', 'F'), ('F', 'E')]
        self.assertListEqual(follow_the_follower2(self.graph),output )

    # Additional 2(b)
    def test_2_follow_the_follower2(self):
        output = [('A', 'B'), ('B', 'A'), ('E', 'C'), ('C', 'E')] 
        self.assertListEqual(follow_the_follower(self.mygraph),output ) 

    # #--- Problem 3----------------------------------
    def test_1_connected(self):
        self.assertTrue(connected(graph, 'A' ,'F'))
        self.assertFalse(connected(graph, 'E' ,'A'))
        self.assertFalse(connected(graph, 'A' ,'H'))
        self.assertTrue(connected(graph, 'H' ,'E'))

    # Additional 3
    def test_2_connected(self):
        self.assertTrue(connected(self.mygraph, 'A' ,'E'))
        self.assertFalse(connected(self.mygraph, 'H' ,'F'))
        self.assertFalse(connected(self.mygraph, 'F' ,'B'))
        self.assertTrue(connected(self.mygraph, 'F' ,'H'))


    #--- Problem 4(a)----------------------------------
    def test_lazy_word_reader(self):
        # lazy_word_reader output
        self.filetokens = ["CptS","355","Assignment","3","-","Python","Warmup","This","is","a","text","test","file","for","CptS","355","-","Assignment","3","-","Python",
                          "Warmup","With","some","repeated","text","for","CptS","355","-","Assignment","3","-","Python","Warmup",".","dot"]
        mywords = lazy_word_reader("testfile.txt")
        mywords.__next__()   # returns CptS
        mywords.__next__()   # returns 355
        mywords.__next__()   # returns Assignment

        rest_of_file = []
        for word in mywords:  
            rest_of_file.append(word)
        self.assertListEqual(rest_of_file,self.filetokens[3:])

    # Additional 4(a)
    def test_lazy_word_reader2(self):
        self.filetokens = ["asad", "dsada", "wqe21", "sdac", ".", "dsa", ".", "a", "sadd", ".", "s1!", "sd", "s", "!!", "dsa", "dsa", "2", "gds"]
        mywords = lazy_word_reader("testcaseq4.txt")
        mywords.__next__()   # returns asad
        mywords.__next__()   # returns dsada
        mywords.__next__()   # returns wqe21
        rest_of_file = []
        for word in mywords:  
            rest_of_file.append(word)
        self.assertListEqual(rest_of_file,self.filetokens[3:])

    #--- Problem 4(b)----------------------------------
    def test_word_histogram(self):
        # histogram output
        self.histogram = [('-', 5), ('3', 3), ('355', 3), ('Assignment', 3), ('CptS', 3), ('Python', 3), ('Warmup', 3), ('for', 2), ('text', 2), ('.', 1), ('This', 1), ('With', 1), ('a', 1), ('dot', 1), ('file', 1), ('is', 1), ('repeated', 1), ('some', 1), ('test', 1)]
        self.assertListEqual(word_histogram(lazy_word_reader("testfile.txt")),self.histogram)
    
    # Additional 4(b)
    def test_word_histogram2(self):
        # histogram output
        self.histogram = set([("asad", 1), ("dsada", 1), ("wqe21", 1), ("sdac", 1), (".", 3), ("dsa", 3), ("a", 1), ("sadd", 1), ("s1!", 1), ("sd", 1), ("s", 1), ("!!", 1), ("2", 1), ("gds", 1)])
        self.assertSetEqual(set(word_histogram(lazy_word_reader("testcaseq4.txt"))),self.histogram)
        
if __name__ == '__main__':
    unittest.main()

