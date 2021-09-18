-- CptS 355 - Lab 1 (Haskell) - Fall 2021
-- Name: Boxiang Lin
-- Collaborated with: N/A

module Lab1
     where


-- 1.insert 
insert :: (Num t1,Eq t1) => t1 -> t2 -> [t2] -> [t2]
insert 0 new_item xs = new_item:xs   --Base 1 (Priority): if we can reach to 0, means N <= Length of List, we insert infront of xs 
insert n new_item [] = [] --Base 2 (Secondary): We can't reach to 0 means N > Length of List, we should not insert
insert n new_item (x:xs) = x : insert (n-1) new_item xs --Recusively sub-list and N counter


-- 2. insertEvery
insertEvery :: (Eq t, Num t) => t -> a -> [a] -> [a]                      
insertEvery n item iL = if n == 0 
                         then insert 0 item iL -- only insert to the head as per instruction     
                         else helper n item iL n 
                              where  -- pass additional argument n => fix_n, to kepp the "Every" range measurement. 
                                   helper 0 item xs fix_n = item:helper fix_n item xs fix_n
                                   helper n item [] fix_n = [] 
                                   helper n item (x:xs) fix_n = x: helper(n-1) item xs fix_n

-- 3. getSales
getSales :: (Num p, Eq t) => t -> [(t, p)] -> p
getSales target [] = 0
getSales target ((x,y):xs) = if target == x 
                              then y + getSales target xs 
                              else getSales target xs  --if match the day add its correspoding day else go for next tuple

                                                
-- 4. sumSales
sumSales:: (Num p)=> String -> String -> [(String,[(String,p)])] -> p
sumSales company day [] = 0 
sumSales company day ((x,y):xs) = if x == company 
                                   then getSales day y + sumSales company day xs 
                                   else sumSales company day xs   
--if match the company we gonna use getScales we defined above, to calculate a list to tuples, then add to the all possible company but else not the same compabt go for next

-- 5. split
split :: Eq a => a -> [a] -> [[a]]
split c (x:xs) = splitHelper c (x:xs) [] 
                 where 
                      splitHelper c [] [] = [] -- handle all [] case
                      splitHelper c [] buf = [reverse buf] --keep it reverse since we are backtracking up
                      splitHelper c (x:xs) buf = if x == c 
                                                   then reverse buf : splitHelper c xs [] 
                                                   else splitHelper c xs (x:buf)


-- 6. nSplit
nSplit :: (Ord t, Num t, Eq a) => a -> t -> [a] -> [[a]]
nSplit c n (x:xs) = nSplitHelper c n (x:xs) [] 
                    where
                         nSplitHelper c n [] [] = [] 
                         nSplitHelper c n [] buf = [reverse buf] 
                         nSplitHelper c n (x:xs) buf = if x == c && n > 0 --split if encounter c and n counter still > 0
                                                         then reverse buf : nSplitHelper  c (n-1) xs [] 
                                                         else nSplitHelper c n xs (x:buf)