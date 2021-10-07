{-
Name: Boxiang Lin
Collaborate: N/A
CPT_S 355 HW2 Haskell
-}

module HW2
     where

{- 1. groupbyNTail - 10%-}

groupbyNTail :: [a] -> Int -> [[a]]
groupbyNTail list n = helper list n [] []
                      where
                           helper [] n acc buf = reverse (reverse buf:acc)  -- buf get cons to acc list in case not perfectly reach n size and return the acc list when backtrack.
                           helper (x:xs) n acc buf | (length buf) >= n = (helper xs n ((reverse buf): acc) [x]) --buf get cons to acc during recursion.
                                                   | otherwise = helper xs n acc (x:buf) --accumulate the buf list.

-----------------------------------------------------------

{- 2.  elemAll and stopsAt  -  20% -}


{- (a)  elemAll - 10%-}
-- please don't include the myCatsLog list in your solution file. 
elemAll :: (Foldable t1, Foldable t2, Eq a) => t1 a -> t2 a -> Bool
elemAll l1 l2 = if False `elem` (boolean l1) then False else True --if there is one false we return false, else true;
                where -- Check if all element in l1 elem in l2, can use foldr to generate a bool list that indicate each element exsitence in l2
                     boolean list = foldr (\x acc -> if x `elem` l2 then True:acc else False:acc) [] l1

{- (b) stopsAt - 10%-}
stopsAt :: (Foldable t1, Foldable t2, Foldable t3, Eq a1) => t3 a1 -> t1 (a2, t2 a1) -> [a2]
stopsAt target routes = foldr(\x acc -> if (isElem x) then (theBus x):acc else acc) [] routes --each x consist of tuple (bus, stations), if target all elem in corresponding bus we add the bus.
                      where 
                           isElem (bus,stations) = if elemAll target stations then True else False  --if our target is all elem in current stations we return True else False
                           theBus (bus,stations) = bus  -- this to just return the name of bus so can added into the result list.

-----------------------------------------------------------

{- 3. isBigger and applyRange - 25% -}

--define the Timestamp datatype
data Timestamp =  DATE (Int,Int,Int) |  DATETIME (Int,Int,Int,Int,Int) 
                  deriving (Show, Eq)
{- (a)  isBigger - 15% -}
isBigger :: Timestamp -> Timestamp -> Bool
isBigger time1 time2 = helper time1 time2 
         where   
               helper (DATE (x1, y1, z1)) (DATE (x2, y2, z2)) = isGreater x1 x2 y1 y2 z1 z2
               helper (DATE (x1, y1, z1)) (DATETIME (x2,y2,z2,h2,m2)) = isGreater x1 x2 y1 y2 z1 z2
               helper (DATETIME (x1,y1,z1,h1,m1))  (DATE (x2, y2, z2)) = isGreater x1 x2 y1 y2 z1 z2
               helper (DATETIME (x1,y1,z1,h1,m1)) (DATETIME (x2,y2,z2,h2,m2)) = isEaxctGreater x1 x2 y1 y2 z1 z2 h1 h2 m1 m2 
               isGreater x1 x2 y1 y2 z1 z2 = if dateSum x1 y1 z1 <= dateSum x2 y2 z2 then False else True 
               isEaxctGreater x1 x2 y1 y2 z1 z2 h1 h2 m1 m2 = if dateTimeSum x1 y1 z1 h1 m1 <= dateTimeSum x2 y2 z2 h2 m2 then False else True
               dateSum x y z = x*30 + y + z*365    --(month day year) to unit of days
               dateTimeSum x y z h m = x*43200+ y*1440 + z*518400 + h*60 + m  --(month day year hour min) to unit of minutes


{- (b) applyRange - 10% -}
applyRange :: (Timestamp, Timestamp) -> [Timestamp] -> [Timestamp]
applyRange (t1,t2) list = filter (\x-> (isBigger x t1) && (isBigger t2 x)) list

-----------------------------------------------------------
{-4 - foldTree, createRTree, fastSearch  - 35%-}

--define Tree and RTree data types
data Tree a = LEAF a | NODE a (Tree a) (Tree a)
               deriving (Show,  Eq, Ord)

data RTree a = RLEAF a | RNODE a (a,a) (RTree a) (RTree a)
                    deriving (Show, Eq, Ord)

{- (a) foldTree - 8% -}

foldTree :: (t -> t -> t) -> Tree t -> t
foldTree op tree = helper op tree
                   where 
                        helper op (LEAF v) = v
                        helper op (NODE a t1 t2) = op a (op (helper op t1) (helper op t2))


{- (b) createRTree - 12% -}
createRTree :: Ord a => Tree a -> RTree a
createRTree (LEAF v) = RLEAF v
createRTree (NODE a t1 t2) = RNODE a (min (theMin t1 t2) a, max (theMax t1 t2) a) (createRTree t1) (createRTree t2) --min, max have to also compare the a, because we are accessing the subtrees
                           where 
                                theMin t1 t2 = min (foldTree min t1) (foldTree min t2)
                                theMax t1 t2 = max (foldTree max t1) (foldTree max t2) 

{- (c) fastSearch - 15% -}
fastSearch::Ord t => RTree t->t->[([Char],t)]
fastSearch tree target = helper tree []
                         where 
                            helper (RLEAF v) acc = ("leaf", v):acc
                            helper (RNODE a (x,y) t1 t2) acc = if target >= x && target <= y 
                                                               then ("node", a):acc ++ (helper t1 acc) ++ (helper t2 acc)
                                                               else ("node", a):acc -- if outside the range we stop and add the current node           

-------------------------------------------------------------------

{- Tree Examples 5% -}
-- include your tree examples in the test file. 
--mybst :: Tree Integer
myBST :: Tree Integer
myBST = NODE 7 (NODE 3 (NODE 1 (LEAF 0) (LEAF 2)) 
                       (NODE 5 (LEAF 4) (LEAF 6))
               ) 
               (NODE 12 (NODE 9 (LEAF 8) (LEAF 11)) 
                        (NODE 14 (LEAF 13) (LEAF 15))
               )

myBT :: Tree String
myBT = NODE "A" (NODE "B" (NODE "D" (LEAF "H") (LEAF "I")) 
                          (NODE "E" (LEAF "J") (LEAF "K"))
                )
                (NODE "C" (NODE "F" (LEAF "L") (LEAF "M")) 
                          (NODE "G" (LEAF "N") (LEAF "O"))
                )

{-Testing your tree functions - 5%-}

-- The Q5 tree get tested by Q4(a,b,c) as additional tests.

