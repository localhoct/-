import random

print("0 Sang...")
print("1 kaqhaz...")
print("2 Gheychi...")
print("\n")
print("3 Exit ")
print("\n")
print('<< faqat adadd ra vared knid masalan: 0 yanni sang >>')
score_player = 0
score_computer = 0
sang = 0
kaghaz = 1
gheychi = 2
while True:
    random_number = random.randint(0, 2)
    if random_number == 0:
        computer_move = sang
    elif random_number == 1:
        computer_move = kaghaz

    elif random_number == 2:
        computer_move = gheychi

    computer = computer_move

    print(f'Computer : {score_computer} | Player : {score_player}')

    if score_player ==3:
        print("\n")
        print('You are win the game')
        break
    elif score_computer == 3:
        print("\n")
        print('computer win the game')
        break
    print("0 sang / 1 kaghaz / 2 gheychi / quit or 3 to quit the game")
    player = input("Make your move : ")
    if player == "3":
        print('bye')
        break
    if player == "quit":
        print('bye')
        break

    if int(player) == computer:
        print("Same Move")
    elif int(player) == sang:
        if computer == gheychi:
            print("You are win!")
            score_player +=1
        elif computer == kaghaz:
            print("Computer win!")
            score_computer +=1
    elif int(player) == kaghaz:
        if computer == sang:
            print("You are win!")
            score_player +=1
        elif computer == gheychi:
            print("Computer win!")
            score_computer +=1
    elif int(player) == gheychi:
        if computer == kaghaz:
            print("You are win!")
            score_player +=1
        elif computer == sang:
            print("Computer win!")
            score_computer +=1
    else:
        print("Error!!!")