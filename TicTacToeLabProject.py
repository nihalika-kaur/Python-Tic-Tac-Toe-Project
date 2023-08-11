def Board(x, o):
    # 1 is true (X) 0 is false (O)
    zero = 'X' if x[0] else ('O' if o[0] else '-')
    one = 'X' if x[1] else ('O' if o[1] else '-')
    two = 'X' if x[2] else ('O' if o[2] else '-')
    three = 'X' if x[3] else ('O' if o[3] else '-')
    four = 'X' if x[4] else ('O' if o[4] else '-')
    five = 'X' if x[5] else ('O' if o[5] else '-')
    six = 'X' if x[6] else ('O' if o[6] else '-')
    seven = 'X' if x[7] else ('O' if o[7] else '-')
    eight = 'X' if x[8] else ('O' if o[8] else '-')
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

#Initialization
winConditions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
win = False
x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
o = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1
print("Welcome to Tic-Tac-Toe")

while win == False:
        Board(x, o)
        if turn % 2 != 0:
            print("")
            print("Player X turn")
            val = int(input("Enter number (1-9): "))
            x[val-1] = 1
            for i in winConditions:
                if (x[i[0]]+x[i[1]]+x[i[2]]) == 3:
                    Board(x, o)
                    print("Player X wins!")
                    quit()
            turn += 1
        if turn == 10:
            Board(x, o)
            print("DRAW")
            win == True
            quit()
        Board(x, o)
        if turn % 2 == 0:
            print("")
            print("Player O turn")
            val = int(input("Enter number (1-9): "))
            o[val-1] = 1
            for i in winConditions:
                if (o[i[0]]+o[i[1]]+o[i[2]]) == 3:
                    Board(x, o)
                    print("Player O wins!")
                    quit()
            turn += 1