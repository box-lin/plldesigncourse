mul x y  = x * y

main = do putStrLn "Enter 2 numbers:"
          a <- readLn
          b <- readLn
          let  s = "What is" ++ show a ++ "*" ++ show b  ++ "?"
             in  putStrLn s
          x <- readLn
          if x == (mul a b)
             then putStrLn "You're right!"
             else putStrLn "You're wrong!"