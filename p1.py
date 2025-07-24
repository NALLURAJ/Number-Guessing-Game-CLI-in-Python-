#GUESSING A NUMBER IN PYTHON USING RANDOM MODULE, CONTITIOAL STATEMENTS AND FUNCTIONS !

import random
ran_num = random.randint(1,100)


def get_inp():
    while True:
        usr_int = input("Enter the Number(b/t 1 to 100) : ")
        try:
            usr_int = int(usr_int)
            return usr_int
        except:
            print("Don't Enter Strings or Float")

def main():
    attempt = 0
    while True:
        usr_int = get_inp()
        attempt += 1

        if usr_int == ran_num :
            print(f"Congratulations, You're guess is right! and you guessed in {attempt} attempts.")
            break
        elif usr_int > ran_num:
            print("Too High")
            attempt +=1
        elif usr_int < ran_num:
            print("Too Low")
            attempt +=1
        else:
            print("Enter a valid input")
    print("✅ Game Over. Thanks for playing!")
main()




