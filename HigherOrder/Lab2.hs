-- CptS 355 - Lab 2 (Haskell) - Fall 2021
-- Name: 
-- Collaborated with: 

module Lab2
     where


-- 1
{- (a) merge2 -}
merge2 [] [] = []
merge2 xs [] = xs
merge2 [] ys = ys
merge2 (x:xs) (y:ys) = x:y : merge2 xs ys 
                         

{- (b) merge2Tail -}
merge2Tail l1 l2 = helper l1 l2 [] 
                   where 
                        helper [] [] acc = reverse acc
                        helper xs [] acc = acc ++ xs
                        helper [] ys acc = acc ++ ys
                        helper (x:xs) (y:ys) acc = helper xs ys (y:x:acc)

{- (c) mergeN -}
mergeN :: [[a]] -> [a]
mergeN lst = foldl merge2 [] lst


-- 2
{- (a) count -}

count :: Eq a => a -> [a] -> Int
count val list = length(filter(\x -> x == val) list)


{- (b) histogram  -}
-- Map will return a list with elements of (sublist count)
-- Use foldr to disregard those duplicate sublist.
histogram :: Eq a => [a] -> [(a, Int)]
histogram lst = foldr (\x acc -> if x `elem` acc then acc else x:acc) [] (map (\x->(x, count x lst)) lst)
     
-- map (\x->(x, count x lst)) lst   返回全tuple带有count
-- unique lst = foldr (\x acc -> if x `elem` acc then acc else x:acc) [] lst   利用foldr进行删除操作

-- 3                
{- (a) concatAll -}
-- concatAll list = foldr(\x acc -> (toString x) ++acc) "" list
--                  where 
--                       toString sublist = foldr (\x acc -> x++acc) "" sublist 


concatAll::[[String]] ->String
concatAll list = foldr(\x acc -> x++acc) "" (goodlist list) --Concate the whole list.
                 where 
                      goodlist lst = map(\x-> toString x) lst -- Good list with all sublists concated
                      toString sublist = foldr (\x acc -> x++acc) "" sublist  -- Concate the sublists 


{- (b) concat2Either -}               
data AnEither  = AString String | AnInt Int 
                deriving (Show, Read, Eq)

concat2Either::   [[AnEither]] -> AnEither
concat2Either list = foldr stringHelper (AString "") (goodlist list ) -- This will concate the all sublists into one AString type data.
                     where 
                          goodlist list = map toString list -- Now this is a goodlist with each sublist x in L has only one AString data
                          toString sublist = foldr stringHelper (AString "") sublist -- for each sublist x in L, we concate all data with AString to one AString data. 
                          stringHelper (AString s1) (AString s2) = AString (s1++s2)
                          stringHelper (AString s1) (AnInt n1) = AString (s1 ++ show n1)
                          stringHelper (AnInt n1) (AString s1) = AString (show n1 ++ s1)
                          stringHelper (AnInt n1) (AnInt n2) = AString (show n1 ++ show n2)

-- 4      
{-  concat2Str -}               
-- concat2Str :: [[AnEither]] -> String
-- concat2Str list = toString (concat2Either list) -- The list got computed concate by previous funcion, now we just need to return its String.
--                      where 
--                           toString (AString theString) = theString

concat2Str list = concatAll (map toString list)   -- now it is a nested list with string, we can use the function concatAll that we previously define to concat them up.
                  where 
                     toString sublist = map each sublist  --map each sublist to string type
                     each (AString s1) = s1      
                     each (AnInt n1) = show n1
        

 

data Op = Add | Sub | Mul | Pow
          deriving (Show, Read, Eq)





evaluate:: Op -> Int -> Int -> Int
evaluate Add x y =  x+y
evaluate Sub   x y =  x-y
evaluate Mul x y =  x*y
evaluate Pow x y = x^y

data ExprTree a = ELEAF a | ENODE Op (ExprTree a) (ExprTree a)
                  deriving (Show, Read, Eq)


-- 5 
{- evaluateTree -}



-- 6
{- printInfix -}



--7
{- createRTree -}
data ResultTree a  = RLEAF a | RNODE a (ResultTree a) (ResultTree a)
                     deriving (Show, Read, Eq)






