def nombre():
    chiffre = 0
    while chiffre < 100:
        chiffre +=1
        if chiffre % 3 == 0 and chiffre % 5 == 0:
            print("FizzBuzz")
        elif chiffre % 3 ==0:
            print("Fizz")
        elif chiffre % 5 == 0:
            print("Buzz") 
        else:
            print(chiffre)
        
        
nombre()
