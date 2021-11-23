-- CptS 355 - Lab 2 (Haskell) - Fall 2021
-- Name: Boxiang Lin
-- Collaborated with: N/A

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
-- Map will return a list with elements of (sublist, count)
-- Use foldr to disregard those duplicate sublist.
histogram :: Eq a => [a] -> [(a, Int)]
histogram lst = foldr (\x acc -> if x `elem` acc then acc else x:acc) [] (map (\x->(x, count x lst)) lst)   


-- 3                
{- (a) concatAll -}
concatAll::[[String]] ->String
concatAll list = foldr(\x acc -> x++acc) "" (goodlist list) --Concat the whole list.
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
                          --stringHelper (AString s1) (AnInt n1) = AString (s1 ++ show n1)
                          stringHelper (AnInt n1) (AString s1) = AString (show n1 ++ s1)
                          --stringHelper (AnInt n1) (AnInt n2) = AString (show n1 ++ show n2)


-- 4      
{-  concat2Str -}               
concat2Str :: [[AnEither]] -> String
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
evaluateTree (ELEAF v) = v
evaluateTree (ENODE op t1 t2) = evaluate op (evaluateTree t1) (evaluateTree t2) -- call the evaluate and deliver the op and x y as where the nodes/leaves bubble up to do the operation.

-- 6
{- printInfix -}
printInfix :: Show a => ExprTree a -> String
printInfix (ELEAF v) = show v
printInfix (ENODE op t1 t2) =  "("++ (printInfix t1)++" `"++(show op)++"` "++(printInfix t2)++")" --print left sub trees then op then right sub trees

--7
{- createRTree -}
data ResultTree a  = RLEAF a | RNODE a (ResultTree a) (ResultTree a)
                     deriving (Show, Read, Eq)

createRTree :: ExprTree Int   -> ResultTree Int
createRTree (ELEAF v) = (RLEAF v)
createRTree (ENODE op t1 t2) = RNODE v (createRTree t1) (createRTree t2)
                               where v = evaluate op (evaluateTree t1) (evaluateTree t2) -- get evaluate function to compute v from its two sub trees





