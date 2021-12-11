import sys
from psParser import read
from psOperators import Operators
from psItems import ArrayValue, Literal, Name, Array,Block
from colors import YELLOW,CEND,BOLD 

testinput1 = """
    /x 4 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """

testinput2 = """
    /x 40 def
    [1 2 3 4] dup 3 [x] putinterval /x exch def
    /g { x stack } def
    /f { /x [10 20 30 40] def g } def
    f
    """

testinput3 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic
    	{ /n 1 def
	      /egg2 { n stack} def
	      n m
	      egg1
          m
	      egg2
	    } def
    n
    chic
        """

testinput4 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x 2 mul } def C } def
    B
    """

testinput5 = """
    /x 2 def
    /n 5  def
    /A { 1  n {x mul} repeat} def
    /C { /n 3 def /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

testinput6 = """
    /myfalse {1 2 eq} def
    /out true def 
    /xand { true eq {pop myfalse} {pop true} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out myfalse def myput } def 
    myfalse  f
    """

testinput7 = """
    /x [1 2 3 4] def
    /A { 0  x {add} forall } def
    /C { /x [10 20 30 40 50] def A stack } def
    /B { /x [6 7 8 9] def /A { x } def C } def
    B
    """

testinput8 = """
    /x [2 3 4 5] def
    /a 10 def  
    /A { x } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x } def /a 5 def C } def
    B
    """

# ------------------------------ Additional TestCases ---------------------------------------#
# Static op stack: 12
# Dynamic op stack: 14
testinput9 = """
        /x 3 def
        /a 9 def
        /b {a x add stack} def
        /c {/x 5 def b} def
        c
"""

# Static op stack: [3 3 3 3]
# Dynamic op stack: [5 5 5 5]
testinput10 = """
        /a [3 3 3 3] def
        /b [1 2 3 4] def
        /c {/b [4 3 2 1] def a stack} def
        /d {/a [5 5 5 5] def c} def
        d
"""

# Static op stack: True
# Dynamic op stack: False
testinput11 = """
        /x {5 5 eq 2 2 eq eq} def
        /y {x stack} def
        /z {/x 5 6 eq def y} def
        z
"""

tests = [testinput1,testinput2,testinput3,testinput4,testinput5,testinput6,testinput7,testinput8, testinput9, testinput10, testinput11]

# program start
if __name__ == '__main__':
    
    psstacks_s = Operators("static")  
    psstacks_d = Operators("dynamic")  
    testnum = 1
    for testcase in tests:
        try:
            print(BOLD+"\n-- TEST {} --".format(testnum)+CEND)
            expr_list = read(testcase)
            print(YELLOW + "\nSTATIC" +CEND)
            # interpret using static scoping rule
            for expr in expr_list:
                expr.evaluate(psstacks_s)
            print(YELLOW + "\nDYNAMIC"+CEND)
            # interpret using dynamic scoping rule
            for expr in expr_list:
                expr.evaluate(psstacks_d)    
            # clear the Stack objects 
            psstacks_s.clearBoth()
            psstacks_d.clearBoth()
        except (SyntaxError, NameError, TypeError, Exception) as err:
            print(type(err).__name__ + ':', err)
        testnum += 1
        # clear the Stack objects 
        psstacks_s.clearBoth()
        psstacks_d.clearBoth()