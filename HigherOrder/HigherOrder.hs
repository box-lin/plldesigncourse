
{- 
Map 的原理：map 运算方法 数组
====
当数组为空, 返回空数组进行叠加
map 运算方法 数组 = 取数组头进运算 : 递归数组尾部

-}
map' :: (t -> a) -> [t] -> [a]
map' op [] = []
map' op (x : xs) = (op x): (map' op  xs) --(op x) 返回 x 运算后的值 从而继续递归 直至条件退出, 后叠加。 

square :: Num b => [b] -> [b]
square lst  = map square lst --传入map
              where square x  =  x*x  -- 运算函数

squareA lst = map(\x -> x*x) lst --匿名函数 (参数->返回值)

-------------------------------------------------------------------------------------------------------------------

{- 
Filter 的原理：map 运算方法 数组 
注意: 运算方法返回一个布尔值
====

当递归条件不符合 返回叠加

如果 op x 返回的是True 我们进行 x: 递归
如果不是则 直接递归
-}

filter' :: (a -> Bool) -> [a] -> [a]
filter' op [] = []
filter' op (x : xs) | (op x)     = x : (filter' op xs)
                    | otherwise  = filter' op xs


odds2 xs = filter isOdd xs
            where isOdd x  = (x `mod` 2) == 1

smallerV lst v = filter (\x -> (x<v)) lst

-----------------------------------------------------------------------------------------------------------------
{-
fold函数： 运算 base 数组 -> base

把base想着accumulator, fold函数的作品 在与 返回我们目的的accumulator.
fold操作是把一个列表聚合成一个值的过程

foldr 正常递归法

foldl tail recursion法
-}

foldr' :: (t1 -> t2 -> t2) -> t2 -> [t1] -> t2
foldr' op base []     = base
foldr' op base (x:xs) = x `op` (foldr' op base xs)


foldl' :: (t1 -> t2 -> t1) -> t1 -> [t2] -> t1
foldl' op base []     = base
foldl' op base (x:xs) =  (foldl' op (base `op` x) xs)


count :: (Foldable t, Eq a1, Num a2) => a1 -> t a1 -> a2
count  e lst = foldr (\x acc -> if e == x then acc + 1 else acc ) 0 lst

copyList2 :: [a] -> [a]
copyList2 xL = reverse (foldl(\xs x -> x:xs) [] xL)

copyList1 :: [a] -> [a]
copyList1 xL = foldr (\x acc -> x:acc) [] xL

