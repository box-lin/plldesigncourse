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
histogram :: Eq a => [a] -> [(a, Int)]
histogram lst = foldr (\x acc -> if x `elem` acc then acc else x:acc) [] (map (\x->(x, count x lst)) lst)
     
-- map (\x->(x, count x lst)) lst   返回全tuple带有count
-- unique lst = foldr (\x acc -> if x `elem` acc then acc else x:acc) [] lst   利用foldr进行删除操作

-- 3                
{- (a) concatAll -}
concatAll::[[String]] ->String
-- concatAll list = foldr(\x acc -> (toString x) ++acc) "" list
--                  where 
--                       toString sublist = foldr (\x acc -> x++acc) "" sublist 


concatAll list = foldr(\x acc -> x++acc) "" (goodlist list)
                 where 
                      goodlist lst = map(\x-> toString x) lst
                      toString sublist = foldr (\x acc -> x++acc) "" sublist 


{- (b) concat2Either -}               
data AnEither  = AString String | AnInt Int
                deriving (Show, Read, Eq)




-- 4      
{-  concat2Str -}               




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






