name = input("type your name: ")
print("welcome",name,"to this adventure")

answer = input("you are on a dirt road,it has come to an end and you can go left or right.which way would you like to go? ").lower()
if answer == "left":
    answer =input("you come to a river,you can walk around it or swim across? Type walk to walk around and to swim across: ")

    if answer == "swim":
        print("you swam across and were eaten by by an alligator.")
    elif answer =="walk":
        print("you walked for many milies,run out of water and you lost the game")

    else:
        print("not a valid option.you lose.")


elif answer == "right":
    answer = input("you come to a bridge,it look wobbly,do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("you go back and lose")
    elif answer =="cross":
        answer = input("you cross the bridge and  meet a staranger.Do you talk to them(yes/no)? ")
        if answer =="yes":
            print("you talk to he stranger and they give yo gold .You Win!")
        elif answer == "no":
            print("you ignore the stranger and they are offended and you lose.")
        else:
            print("not a valid option.you lose.")

    else:
        print("not a valid option.you lose.")
else:
    print("not a valid option.you lose.")
print("thanks you for trying",name)