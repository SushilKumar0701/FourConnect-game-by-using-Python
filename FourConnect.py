cols=7
rows=6
class Board():
    def __init__(self):
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.turns=0
        self.last_move=[-1,-1] #row, col

    def print_board(self):
        #number the column
        print('\n')
        for c in range(cols):
            print(f" ({c+1})", end="")
        print("\n")
        #print the slots of the game board
        for r in range(rows):
            print('|',end="")
            for c in range(cols):
                print(f" {self.board[r][c]} |", end="")
            print("\n")
        print(f"{'_' * 35}\n")

    def which_turn(self):
        players = ['X','O']
        return players[self.turns%2]

    def turn(self, column):
        #search from the bottom up
        for r in range(rows-1,-1,-1):
            if self.board[r][column] == ' ':
                self.board[r][column]= self.which_turn()
                self.last_move=[r,column]

                self.turns +=1
                return True
        return False

    def in_bounds(self, r, c):
        return (r >= 0 and r < rows and c >= 0 and c < cols)

    def check_winner(self):
        last_row = self.last_move[0]
        last_col = self.last_move[1]
        last_letter = self.board[last_row][last_col]

        #[r,c] direction, matching letter count, locked bool

        directions = [
            [[-1, 0], 0, True],
            [[1, 0], 0, True],
            [[0, -1], 0, True],
            [[0, 1], 0, True],
            [[-1, -1], 0, True],
            [[1, 1], 0, True],
            [[-1, 1], 0, True],
            [[1, -1], 0, True]
        ]
        #Search outwards looking for matching letters
        for a in range(4):
            for d in directions:
                r = last_row + (d[0][0] * (a+1))
                c = last_col +(d[0][1] * (a+1))

                if d[2] and self.in_bounds(r,c) and self.board[r][c] == last_letter:
                    d[1] +=1
                else:
                    #stop searching in this direction
                    d[2] = False

        #Check possible direction pairs for 4 pieces in a row
        for i in range(0, 7, 2):
            if(directions[i][1] + directions[i+1][1] >= 3):
                self.print_board()
                print(f"{last_letter} is the winner")
                return last_letter
        #Did not find a winner
        return False


def play():
    game = Board()
    game_over = False
    while not game_over:
        game.print_board()

        valid_move = False
        while not valid_move:
            user_move = input(f"{game.which_turn()}'s turn : ")
            try:
                valid_move = game.turn(int(user_move) -1)
            except:
                print(f"Please choose a number between 1 and {cols}")

        game_over = game.check_winner()

        if not any(' ' in x for x in game.board):
            print("The game is draw....")
            return




if __name__=='__main__':
    play()