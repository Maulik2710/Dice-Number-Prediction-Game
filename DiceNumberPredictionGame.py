import random
print("\n")
print("In this game you have to predict that the number on the dice is greater than the previous number or not!\n Have Fun!!")
print("\n")
input_from_user = int(input("Give me the number between 1 to 6: \n"))
if((input_from_user > 6) or (input_from_user < 1)):
    print("!!! Invalid entry !!!")
    print("Your input should between 1 to 6!")
    input_from_user = int(input("Give me the number between 1 to 6: \n"))
point = 0

while True:
    predict = input("Now you have to predict that the dice's number is greater than the previous number or Not; \n if Yes then give input as 'A',\n if No then give input as 'B',\n or if you think it's equal then give input as 'C': \n")
    print("\n")
    random_number = random.randint(1, 6)
    print(f"The new dice number is: {random_number}")

    if ((random_number > input_from_user and predict == "A") or
        (random_number < input_from_user and predict == "B") or
        (random_number == input_from_user and predict == "C")):
        print("Congratulations,\n you are right!\n You got a point.")
        point += 1
        print("Your points are: ", point)
        print("\n")
    else:
        print("Ohh! you lost!\n Better luck next time!")
        print("Your total score is: ", point)
        break

    # Update input_from_user for the next round
    input_from_user = random_number
