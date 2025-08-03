board = [' ' for _ in range(9)]

symbol = {
    'X': '❌',
    'O': '😊',
    ' ': '⬜'
}

def printBoard():
    print("\n")
    for i in range(3):
        print(" " + " | ".join(symbol[board[j]] for j in range(i * 3, i * 3 + 3)))
        if i < 2:
            print("---|---|---")
    print("\n")

def Winner(player):
    Combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)           
    ]
    for combo in Combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def Draw():
    return ' ' not in board

def playGame():
    currentPlayer = 'X'
    
    print("🎮 Welcome to Tic Tac Toe!")
    print("❌ = Player X\n😊 = Player O\n")

    while True:
        printBoard()
        try:
            move = int(input(f"Player {symbol[currentPlayer]}, choose a position (1–9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Enter a valid number between 1 and 9.")
            continue

        board[move] = currentPlayer

        if Winner(currentPlayer):
            printBoard()
            print(f" Player {symbol[currentPlayer]} wins! Congratulations!")
            break
        elif Draw():
            printBoard()
            print("It's a draw! Well played.")
            break

        currentPlayer = 'O' if currentPlayer == 'X' else 'X'

playGame()
