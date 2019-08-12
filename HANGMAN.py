def hangman(word):
    wrong = 0
    stages = ["",
              "|_________|",
              "|         |",
              "|    |    |",
              "|    O    |",
              "|   /|\   |",
              "|   / \   |",
              "|         |",
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("wyselitsa!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Vvedite bookwu: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong +=1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("YOU WIN! The word was: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! Thw word was: {}.".format(word))
hangman("путин")

