compareBig::Double->Double->Double
compareBig x  y =
    if x < y
        then y
    else if x == y
        then  x + y
    else x

main = do
    print $ compareBig 2.4 5.3
    print $ compareBig 5.5 5.7
    print $ compareBig 1.2 1.2