a=int(input("Guess A Number: "))
if a==20:
    print("!!You Win!! :)")
else:
    if a < 20:
        print("You Guess The Lower Number!")
    else:
        print("You Guess The Higher Number!")