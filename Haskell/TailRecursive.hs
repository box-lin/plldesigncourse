-- CptS 355 - Sample Functions

module TailRecursive
     where

import Data.Char

-- non-tail recursive "reverse"
myreverse [] = []
myreverse (x:xs) = x `snoc` (myreverse xs)
                  where 
                     snoc x xs = xs `myappend` [x]
                     myappend [] list = list
                     myappend (x:xs) list = x:(myappend xs list)
     

-- tail recursive "reverse"
fastreverse iL =  revappend iL []
                where 
                        revappend [] list = list
                        revappend (x:xs) list = (revappend xs (x:list))

-- "numbers2Sum" that takes an Int list "iL" and a Int value "n", 
-- and returns the ordered values from the input list that add up to less than or equal to  n.

-- Examples:
-- l1 = numbers2Sum [1,2,3,4,5,6,7]  15   -- [1,2,3,4,5]
-- l2 = numbers2Sum [1,2,3,4,5,6,7]  14   --  [1,2,3,4]
numbers2Sum [] n = []
numbers2Sum (x:xs) n | (n-x) >= 0  =  x:(numbers2Sum xs (n-x))   -- where the sum of the elements are less than n
                     | otherwise =   []     -- where the sum of the elements are greater than or equal to n

-- Examples:
-- l1 = numbers2SumTail [1,2,3,4,5,6,7]  15  []  -- [1,2,3,4,5]
-- l2 = numbers2SumTail [1,2,3,4,5,6,7]  14  [] --  [1,2,3,4]
numbers2SumTail [] n acc = reverse acc
numbers2SumTail (x:xs) n acc | (n-x) >= 0  =  (numbers2SumTail xs (n-x) (x:acc))  
                             | otherwise =   reverse acc    