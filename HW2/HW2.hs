module HW2
     where

{- 1. groupbyNTail - 10%-}

groupbyNTail :: [a] -> Int -> [[a]]
groupbyNTail list n = helper list n [] []
                      where
                           helper [] n acc buf = (reverse buf):acc  -- buf get cons to acc list in case not perfectly reach n size and return the acc list when backtrack.
                           helper (x:xs) n acc buf | (length buf) >= n = reverse (helper xs n ((reverse buf): acc) [x]) --buf get cons to acc during recursion.
                                                   | otherwise = helper xs n acc (x:buf) --accumulate the buf list.

-----------------------------------------------------------

{- 2.  elemAll and stopsAt  -  20% -}


{- (a)  elemAll - 10%-}
-- please don't include the myCatsLog list in your solution file. 
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

{- (b) applyRange - 10% -}


-----------------------------------------------------------
{-4 - foldTree, createRTree, fastSearch  - 35%-}

--define Tree and RTree data types
data Tree a = LEAF a | NODE a (Tree a) (Tree a)
               deriving (Show,  Eq, Ord)

data RTree a = RLEAF a | RNODE a (a,a) (RTree a) (RTree a)
                    deriving (Show, Eq, Ord)

{- (a) foldTree - 8% -}

{- (b) createRTree - 12% -}

{- (c) fastSearch - 15% -}

-------------------------------------------------------------------

{- Tree Examples 5% -}
-- include your tree examples in the test file. 

{-Testing your tree functions - 5%-}


