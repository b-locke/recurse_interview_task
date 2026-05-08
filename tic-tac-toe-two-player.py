def gameLoop():
    game_complete = False
    game_board = [["_" for y in range(0,3)] for x in range(0,3)]
    game_board_ref = [[(x, y) for y in range(0, 3)] for x in range(0,3)]
    game_board_ref = game_board_ref[0] + game_board_ref[1] + game_board_ref[2]
    padding = ''.join(['*' for x in range(40)])
    msg = "\n" + padding + "\nThat move is not available or is incorrectly formatted. Please try again.\n" + padding + "\n"
    current_player = 1

    def print_game_board():
        for row in list(reversed(game_board)): 
            print(row)
        print("")

    while game_complete == False:

        print_game_board()

        user_symbol = 'X' if current_player == 1 else 'O'

        user_move = input(f"It's player {current_player}'s move.\n\nWhere would you like to place you piece?\n\n0,0 is the bottom left. 0,2 is the top left.\n\n")
        print("")
        
        try:
            user_move_coordinates = user_move.split(',')
            x = int(user_move_coordinates[1])
            y = int(user_move_coordinates[0])

            if game_board[x][y] == '_':

                game_board[x][y] = user_symbol
                game_board_ref.remove((x,y))

                lines = [
                    [game_board[0][0], game_board[0][1], game_board[0][2]],
                    [game_board[1][0], game_board[1][1], game_board[1][2]],
                    [game_board[2][0], game_board[2][1], game_board[2][2]],
                    [game_board[0][0], game_board[1][0], game_board[2][0]],
                    [game_board[0][1], game_board[1][1], game_board[2][1]],
                    [game_board[0][2], game_board[1][2], game_board[2][2]],
                    [game_board[0][0], game_board[1][1], game_board[2][2]],
                    [game_board[2][0], game_board[1][1], game_board[0][2]]
                ]

                for l in lines:
                    li = ''.join(l)
                    if li == "XXX":
                        print(f"\nPlayer {current_player} wins!\n")
                        print_game_board()
                        game_complete = True
                
                if len(game_board_ref) < 1 and game_complete == False:
                    print("\nNo moves remain!\n")
                    print_game_board()
                    game_complete = True
 
                current_player = 2 if current_player == 1 else 1

            else:
                print(msg)

        except:
            print(msg)

def mainLoop():
    user_input = "y"
    print("\nWelcome to space invaders!\n")
    while user_input != "n":
        gameLoop()
        user_input = input("Would you like to play again? y/n")

mainLoop()


