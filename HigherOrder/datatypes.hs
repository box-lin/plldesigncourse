type Point = (Float, Float)
type Line  = (Point, Point)

type Node a = (a,a)
type Edge a = (Node a, Node a)

n1 = (1,2)::(Node Int)
n2 = (4,8)::(Node Int)
n3 = (6,9)::(Node Int)
e1 = (n1,n2)::(Edge Int)
e2 = (n2,n3)::(Edge Int)

type Graph a = [Edge a]

g = [e1,e2]

{- ***************************************************** -}

data Days = Sunday  | Monday  | Tuesday  | Wednesday  | Thursday  | Friday  | Saturday
            deriving (Show,Eq)

-- returns Sunday :: Days

isWeekday :: Days -> Bool
isWeekday Sunday   = False
isWeekday Saturday = False
isWeekday _        = True

isWeekday2 :: Days -> Bool
isWeekday2 day = not $ day `elem` [Saturday, Sunday]

{- ***************************************************** -}

data Money = NONE | COIN Int | BILL Int
             deriving (Eq, Show, Ord)

x = (COIN 10)
y = (BILL 20)
z = NONE
-- :t x          -- returns x::Money 

-- (COIN 5) == (BILL 5)
amount :: Fractional p => Money -> p
amount (NONE) = fromIntegral(0)
amount (COIN x) = fromIntegral(x) /100.0
amount (BILL x) = fromIntegral(x) 

-- amount (COIN 25) -- returns 0.25

{- ***************************************************** -}

data MaybeInt = JustInt Int | NoInt deriving (Show, Eq)
data MaybeStr = JustStr String | NoStr deriving (Show, Eq)
data MaybeDouble = JustDouble Double | NoDouble  deriving (Show, Eq)

-- Maybe is a built-in type in Prelude
-- data Maybe a = Just a  | Nothing  
--                deriving (Show, Eq, Ord)

a = (Just 10)      -- :t a  returns a :: Num a => Maybe a
b = (Just "ten")   -- :t b  returns b :: Maybe [Char] 
c = Nothing        -- :t d  returns d :: Maybe a
d = (Just [1,2,3]) -- :t e  returns e :: Num a => Maybe [a]

head' :: [a] -> Maybe a
head' [] = Nothing 
head' (x:xs) = (Just x)

-- head' [[1],[2,3]]  -- returns Just [1]
-- head' [] -- returns Nothing

last' :: [a] -> Maybe a
last' [] = Nothing
last' [x] = (Just x)
last' (x:xs) = last' xs

-- last [[1],[2,3]]  -- returns Just [2,3]
-- last [] -- returns Nothing

addMaybe :: Maybe a -> Maybe a -> Maybe a

addMaybe Nothing Nothing = Nothing
addMaybe Nothing (Just v) = (Just v)
addMaybe (Just v) Nothing =  (Just v)
addOpaddMaybetion (Just v1) (Just v2) =  (Just (v1+v2))

-- addMaybe (Just 20) (Just 10)  -- returns Just 30
-- addMaybe (Just 20) Nothing  -- returns Just 20

{- ***************************************************** -}

data MyList a = EMPTY | CONS a (MyList a)

-- :t (:)
-- (:) :: a -> [a] -> [a]
-- :t CONS
-- CONS :: a -> MyList a -> MyList a

{- ***************************************************** -}

-- Binary Int Tree
data IntTree = Leaf Int | Node (IntTree)  (IntTree)
               deriving (Show, Eq)

l1 = Leaf 3
l2 = Leaf 4
tree1 = Node l1 l2

tree1' = Node (Leaf 3) (Leaf 4)
tree2 = Node (Node (Leaf 5) (Leaf 6)) (Leaf 4)

-- Polymorphic binary tree
data Tree a = LEAF a | NODE (Tree a) (Tree a)
              deriving (Show, Eq)

l1' = (LEAF "three");
l2' = (LEAF "four");
tree3 = NODE l1' l2'

tree4 = NODE (NODE (LEAF "one") (LEAF "two")) (NODE (LEAF "three") (LEAF "four"))

-- Polymorphic ternary tree1
data TriTree a = TLEAF a | TNODE (TriTree a) (TriTree a) (TriTree a)
               deriving (Show, Eq)

ttree = TNODE (TLEAF 9) (TNODE (TLEAF 8) (TLEAF (-1)) (TLEAF 7)) (TNODE (TLEAF 3) (TLEAF 4) (TNODE (TLEAF 1) (TLEAF (-8) ) (TLEAF 5) ))               

data BinTree a = BLEAF a | BNODE a (BinTree a) (BinTree a)

btree = BNODE "one" (BLEAF "two") (BNODE "three" (BLEAF "four") (BLEAF "five") )




