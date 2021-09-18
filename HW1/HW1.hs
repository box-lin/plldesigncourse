-- CptS 355 - Fall 2021 -- Homework1 - Haskell
-- Name: Boxiang Lin
-- Collaborators: 

module HW1
     where

--Q1 everyOther
{- Using the tail recursion to accumulate the result while during the recursive steps. Founded that []:num does causes errors so dedicde to num:[], where [] is the 
   accumulation list and num is the iL head. This will end up with the reverse order, so decided to reverse the accumulation list when at the base step. Hence, the 
   accumulation result is computed when backtrack up.
-}

-- everyOther :: [a] -> [a]
-- everyOther iL = helper iL [] 0 -- evens odds are everyother, so using a "n" counter to help distinguish the correct spot to put the element to the accumulation list.
--                 where
--                      helper [] acc n = reverse acc
--                      helper (x:xs) acc n = if even n then helper xs (x:acc) (n+1)
--                                            else helper xs acc (n+1)

everyOther :: [a] -> [a]
everyOther iL = helper iL 0 -- evens odds are everyother, so using a "n" counter to help distinguish the correct spot to put the element to the accumulation list.
                where
                     helper [] n = []
                     helper (x:xs) n = if even n then x: helper xs (n+1) 
                                       else helper xs (n+1)


-- Q2(a) eliminateDuplicates
-- eliminateDuplicates :: Eq a => [a] -> [a]
-- eliminateDuplicates iL = helper iL []
--                          where 
--                               helper [] acc = reverse acc
--                               helper (x:xs) acc = if x `elem` xs then helper xs acc
--                                                   else helper xs (x:acc)

eliminateDuplicates [] = []
eliminateDuplicates (x:xs) =  if x `elem `xs then eliminateDuplicates xs else x: eliminateDuplicates xs 


-- Q2(b) matchingSeconds
matchingSeconds name [] = []
matchingSeconds name ((x,y):xs) = if name == x then  y: matchingSeconds name xs else matchingSeconds name xs 


-- Q2(c) clusterCommon
clusterCommon::(Eq t) => [(t,a)]->[(t,[a])]   -- clusterCommon::(Eqt,Eqa)=>[(t,a)]->[(t,[a])] also compatible 
clusterCommon [] = []
clusterCommon ((x,y):xs) = (x, y: matchingSeconds x xs) : clusterCommon (eliminateSame x xs)
                           where 
                           eliminateSame prev [] = []
                           eliminateSame prev ((x,y):xs) = if x == prev then eliminateSame prev xs else (x,y):eliminateSame prev xs 


-- Q3 maxNumCases
maxNumCases::(Num p,Ord p,Eq t)=>[(a,[(t,p)])]->t->p
maxNumCases cdcData month = helper cdcData month [] 
                            where
                                 helper [] month acc = maximum acc
                                 helper ((x,y):xs) month acc = helper xs month (county month y:acc)
                                 county month [] = 0 -- when no month founded means that month is 0
                                 county month ((x,y):xs) = if x == month then y else county month xs


-- Q4 groupIntoLists

groupIntoLists list = helper list [] 1 
                    where 
                         helper [] [] n = []
                         helper [] buf n = [reverse buf]
                         helper (x:xs) buf n = if length buf >= n then reverse buf : helper xs [x] (n+1) 
                                               else helper xs (x:buf) n

-- Q5 getSlice
getSlice:: Eq a=>(a,a)->[a]->[a]
getSlice (i,j) [] = [] -- this handles not i in list 
getSlice (i,j) (x:xs) | i == x && i /= head xs = res j xs -- res will return the list that end before j
                      | otherwise = getSlice (i,j) xs  -- if not encouter i keep recursively digging
                      where 
                           res j [] = []  -- there is not j in list so at the end return whole list that res receive 
                           res j (x:xs) = if j == x then [] else x: res j xs -- as soon we encounter x we form list to return



                         
                         