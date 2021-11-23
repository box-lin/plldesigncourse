
data Tree a = LEAF | NODE a (Tree a) (Tree a )  
                    deriving (Show, Eq)


repla (LEAF) x y = LEAF
repla (NODE a t1 t2) x y = if x == a then NODE y (repla t1 x y) (repla t2 x y) else NODE a (repla t1 x y) (repla t2 x y)
 
myBST = NODE 7 (NODE 3 (NODE 1 (LEAF) (LEAF)) 
                       (NODE 7 (LEAF) (LEAF))
               ) 
               (NODE 12 (NODE 9 (LEAF) (LEAF)) 
                        (NODE 7 (LEAF) (LEAF))
               )


 
fuc :: (t -> a) -> (t, t) -> [a]
fuc f (a,b) = [f a,f b]

me a b = [fuc a,fuc b]