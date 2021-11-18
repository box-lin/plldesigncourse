from psParser import read
from psOperators import Operators
psstacks = Operators()
testinput1 = """
    1 2 3 true
"""

expr_list = read(testinput1)
print(expr_list)
# for expr in expr_list:
#     expr.evaluate(psstacks)
# print(psstacks.opstack)
# print(psstacks.dictstack)

# if '/x' in psstacks.dictstack:
#     print("yes")