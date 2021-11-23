-- CptS 355 - Sample Functions

module HigherOrder_lecture
     where

import Data.Char

-- ======= Examples of "mapping" functions

--copyList
copyList [] = []
copyList (x:xs)  = x : (copyList xs)

-- allSquares
allSquares :: Num a => [a] -> [a]
allSquares [] = []
allSquares (x : xs) = x * x : allSquares xs
 

-- strToUpperq
strToUpper :: String -> String
strToUpper [] = []
strToUpper (chr:xs) = (toUpper chr) : (strToUpper xs)

-- implement our own map
map' op [] = []
map' op (x : xs) = (op x): (map' op  xs)

-- rewrite allSquares using map

allSquares2 xs  = map square xs
                   where square x  =  x*x

-- rewrite allSquares using map and anonymous function
allSquares3 xs  = map (\x -> x*x) xs
                   
-- multiplyBy 
multiplyBy n x =  x*n

multiplyAll xs n = map  (multiplyBy n)  xs

-- multiplyAll xs n = map  (\x  -> x*n)  xs

-- ======= Examples of "filtering" functions
-- implement our own filter
filter' :: (a -> Bool) -> [a] -> [a]
filter' op [] = []
filter' op (x : xs) | (op x)     = x : (filter' op xs)
                    | otherwise  = filter' op xs

-- odds
odds [] = []
odds (x:xs)  | ((x `mod` 2) == 1) = x: (odds xs)
             |  otherwise = (odds xs)

-- rewrite "odds" using filter
odds2 xs = filter isOdd xs
            where isOdd x  = (x `mod` 2) == 1

-- rewrite "odds" using filter and anonymous function
odds3 xs = filter (\x -> (x `mod` 2) == 1) xs

-- filter if smaller than v
filterSmaller [] v = [] 
filterSmaller (x:xs) v | (x >= v) = x:(filterSmaller xs v)
                       | otherwise = (filterSmaller xs v)

-- rewrite filterSmaller using filter 
filterSmaller2 xs v = filter (isSmaller v)  xs
                       where isSmaller v x = (x >= v) 

-- rewrite filterSmaller using filter  and anonymous function
filterSmaller3 xs v = filter (\x -> (x >= v))  xs

--extractDigits
extractDigits :: String -> String
extractDigits [] = []
extractDigits (chr:xs) | isDigit chr = chr : extractDigits xs
                         | otherwise = extractDigits xs



-- ======= Examples of "reduction" functions
addup []     = 0
addup (x:xs) = x + (addup xs)

mul []     = 1
mul (x:xs) = x * (mul xs)

minList1 []     = maxBound
minList1 (x:xs) = x `min` (minList1 xs)

--alternative implementation for minList
minList2 []     = error "List is empty"
minList2 [x]    = x 
minList2 (x:xs) = x `min` (minList2 xs)

reverse' [] = []
reverse' (x:xs) = x `snoc` (reverse' xs)
                  where 
                       snoc x xs = xs ++ [x]

-- implement our own foldr
foldr' op base []     = base
foldr' op base (x:xs) = x `op` (foldr' op base xs)

-- implement our own foldl
foldl' op base []     = base
foldl' op base (x:xs) =  (foldl' op (base `op` x) xs)

cons x xs = x:xs
mystery xL = foldr cons [] xL

cons2 xs x = x:xs
mystery2 xL = foldl cons2 [] xL




-- implement cons0_all
-- cons0_all [[1,2],[3],[4,5],[]]   --  [[0,1,2],[0,3],[0,4,5],[0]]
cons0 xs = 0:xs
cons0_all iL = map cons0 iL


-- implement consX_all
--  consX_all "0"  [["1"],["2","3"],[]] --  [["0","1"],["0","2","3"],["0"]]
consX x xs = x:xs
consX_all v iL = map (consX v) iL

consX_all2 v iL = map (\xs -> v:xs) iL

-- implement maxLL
-- maxLL [[6,4,2],[-1,7],[1,3],[]] --  7

-- implement maxL

maxLL iL = maxL (map maxL iL)
            where maxL xs = foldr gt (minBound::Int) xs
                  gt x y = if x < y then y else x
















-- maxLL xs = maxL ( map maxL xs ) 
--             where 
--                  maxL xs = foldr gt (minBound::Int) xs 
--                             where gt x y = if x < y then y else x 

-- foldl (+) 0 [1,2,3] 
-- foldl (+) (0+1) [2,3] 
-- foldl (+) (0+1+2) [3] 
-- foldl (+) (0+1+2+3) [] 
-- (0+1+2+3)= 6