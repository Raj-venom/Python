import random

def value(choose):

    if choose == 1:
        return "Snake"
    elif choose == 2:
        return "Water"
    elif choose == 3:
        return "Gun"
    else:
        return "choose a correct option!"



def main(comp, user):
    
    comp = value(comp)
    user = value(user)

    print(f"Computer choosed:{comp}")
    print(f"You choosed:{user}")


    if comp == "Snake":
        if user == "Snake":
            return None
        elif user == "Water":
            return False
        elif user == "Gun":
            return True

    if comp == "Water":
        if user == "Water":
            return None
        elif user == "Gun":
            return False
        elif user == "Snake":
            return True

    if comp == "Gun":
        if user == "Gun":
            return None
        elif user == "Snake":
            return False
        elif user == "Water":
            return True
    



comp = random.randint(1,3)
user = int(input("Choose Snake(1), Water(2), Gun(3): "))
print()


result = main(comp, user)


if result:
    print("You won!!")

elif result == None:
    print("It's Tie")

elif result == False:
   
    print("YOu loose")
