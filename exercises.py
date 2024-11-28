class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print('Tie game!')
        elif self.winner:
            print(f'{self.winner} wins the game!')
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f'Enter a valid movie (example: A1): ').lower()
            if move in ('a1','b1','c1','a2','b2','c2','a3','b3','c3') and self.board[move]==None:
                self.board[move] = self.turn
                break
            else:
                print('invalid input')
    
    def check_for_winner(self):
        winning_combos = [
            ('a1','b1','c1'),
            ('a2','b2','c2'),
            ('a3','b3','c3'),
            ('a1','a2','a3'),
            ('b1','b2','b3'),
            ('c1','c2','c3'),
            ('a1','b2','c3'),
            ('c1','b2','a3')
        ]
        for a,b,c in winning_combos:
            if self.board[a] and (self.board[a] == self.board[b] == self.board[c]):
                self.winner = self.turn
                break
            
    def check_for_tie(self):
        if self.board['a1'] != None and self.board['b1'] != None and self.board['c1'] != None and self.board['a2'] != None and self.board['b2'] != None and self.board['c2'] != None and self.board['a3'] != None and self.board['b3'] != None and self.board['c3'] != None and self.winner == None:
            self.tie = True

    def switch_turn(self):
        if self.turn=='X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def play_game(self):
        print("Shall we play a game?")
        while self.winner == None and self.tie == False:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
        self.render()

game_instance = Game()
game_instance.play_game()

