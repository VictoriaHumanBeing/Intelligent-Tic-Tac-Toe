import random

import Game_Theory

#define the function to draw the board 
def draw_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-'*11)
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-'*11)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


#define the sequence for who goes first
def who_goes_first():
    return 'computer' if random.randint(0, 1) == 0 else 'player'

#return "y" if player play again
#The input not start wuth y will be treat as no, eg: 12346
def play_again():
    # This function
    print('Do you want to play again? (Yes or No)')
    return input().lower().startswith('y')

#The finction to define the next move
def make_move(board, letter, move):
    """ Places a move onto the board """
    board[move] = letter

#Identify the winner
def is_winner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or  # across the top
            (board[4] == letter and board[5] == letter and board[6] == letter) or  # across the middle
            (board[1] == letter and board[2] == letter and board[3] == letter) or  # across the bottom
            (board[7] == letter and board[4] == letter and board[1] == letter) or  # down the left side
            (board[8] == letter and board[5] == letter and board[2] == letter) or  # down the middle
            (board[9] == letter and board[6] == letter and board[3] == letter) or  # down the right side
            (board[7] == letter and board[5] == letter and board[3] == letter) or  # diagonal
            (board[9] == letter and board[5] == letter and board[1] == letter))  # diagonal

#duplicate the board
def get_board_copy(board):
    duplicate_copy_board = []
    for i in board:
        duplicate_copy_board.append(i)
    return duplicate_copy_board

#check weather space is empty, return T is space is empty
def is_space_free(board, move):
    return board[move] == ' '


def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

#move ramdomly
def choose_random_move_from_list(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    return random.choice(possible_moves) if len(possible_moves) != 0 else None

#give computer a letter to play the game 
def __get_computer_move(board, computer_letter):
    player_letter = 'O' if computer_letter == 'X' else 'X'

    # First, check if the computer can win in the next move
    #
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    # Second, check if the player could win on their next move, and block it
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # Third, try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move:
        return move

    # Fourth, try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Finally, make a move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    """
    Check whether has no moves value.
    :param board: the board
    :return: Return True if every space on the board has been taken. Otherwise return False.
    """
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

#Convert board[0-9] to minimax_board[i][j]
def get_computer_move(board, computer_letter):
    #Create the empty minimaxboard
    minimax_board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]
    #Convert board to minimaxborad
    minimax_board[0][0] = board[7].lower() if board[7] != ' ' else '_'
    minimax_board[0][1] = board[8].lower() if board[8] != ' ' else '_'
    minimax_board[0][2] = board[9].lower() if board[9] != ' ' else '_'
    minimax_board[1][0] = board[4].lower() if board[4] != ' ' else '_'
    minimax_board[1][1] = board[5].lower() if board[5] != ' ' else '_'
    minimax_board[1][2] = board[6].lower() if board[6] != ' ' else '_'
    minimax_board[2][0] = board[1].lower() if board[1] != ' ' else '_'
    minimax_board[2][1] = board[2].lower() if board[2] != ' ' else '_'
    minimax_board[2][2] = board[3].lower() if board[3] != ' ' else '_'
    #export function from Game_Theory file and define as best_move
    best_move = Game_Theory.find_best_move(minimax_board)
    #covert the best_move to position on board[0-9]
    if best_move == (0, 0):
        return 7
    if best_move == (0, 1):
        return 8
    if best_move == (0, 2):
        return 9
    if best_move == (1, 0):
        return 4
    if best_move == (1, 1):
        return 5
    if best_move == (1, 2):
        return 6
    if best_move == (2, 0):
        return 1
    if best_move == (2, 1):
        return 2
    if best_move == (2, 2):
        return 3


def main():
    """ Mainline driver to the Tic-Tac-Toe game. """
    print('-' * 26)
    print('Welcome to Tic Tac Toe!')
    print('--------------------------')

    while True:
        board = [' '] * 10
        #board = [
        #['X', '_', 'O'],
        #['_', '_', '_'],
        #['_', '_', '_']]

        # player_letter, computer_letter = input_player_letter()
        player_letter, computer_letter = 'O', 'X'
        turn = who_goes_first()
        print('The ' + turn + ' will go first.')
        game_is_playing = True

        while game_is_playing:
            if turn == 'player':
                draw_board(board)
                move = get_player_move(board)
                make_move(board, player_letter, move)

                if is_winner(board, player_letter):
                    draw_board(board)
                    print('Congratulations! You have won!')
                    game_is_playing = False
                else:
                    if is_board_full(board):
                        draw_board(board)
                        print('Nice game, but we have a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                move = get_computer_move(board, computer_letter)
                make_move(board, computer_letter, move)

                if is_winner(board, computer_letter):
                    draw_board(board)
                    print('Aw, you lost. The computer has beaten you!')
                    game_is_playing = False
                else:
                    if is_board_full(board):
                        draw_board(board)
                        print('Nice game, but we have a tie!')
                        break
                    else:
                        turn = 'player'

        if not play_again():
            break


if __name__ == '__main__':
    main()
