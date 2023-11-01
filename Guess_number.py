def guess_a_number() :
    print("""Structure :
-You have 3 chance to guess
-After a third guess if you can't guess the right number you will lose
-The program helps you to find the number""")
    import random
    number = random.randint(0 , 100)
    user = int(input("-guess your number: "))
    guess = 0
    while user != number :
        if user > number :
            print("Your guess is bigger than number")
            guess += 1
            user = int(input("-guess your number: "))
        elif user < number :
            print("Your guess is smaller than number")
            guess += 1
            user = int(input("-guess your number: "))
        if user == number :
            print("You are win")
            break
        elif guess == 2:
            print("You are losing")
            break

guess_a_number()