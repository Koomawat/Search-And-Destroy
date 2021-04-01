from more_termcolor.colors import brightred, brightgreen, brightyellow, brightblue, brightmagenta, brightcyan

def printBoard(board):

    n = len(board)
    print(" "*(len(str(n))+1), end='')
    for i in range(n):
        if i >= 10: 
            i = i-(10*(int(i/10)))
        print(str(i) + "  ", end='')
    print()

    for i in range(len(board)):
        row = ""
        print(str(i).zfill(len(str(n))) + "|", end='')
        for j in range(len(board)):
            current = str(board[i,j])
            if (current) == 'F':
                row += brightgreen(current) + "  "
            elif (current) == 'f':
                row += brightyellow(current) + "  "
            elif (current) == 'H':
                row += brightred(current) + "  "
            elif (current) == 'C':
                row += brightcyan(current) + "  "
            else:
                row += current + "  "

        print(row)
    print()

    return 
