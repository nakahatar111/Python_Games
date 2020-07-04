class TicTacToe:
    board = [" "] * 10
    player1 = "X"
    player2 = "O"
    db = False
    playersTurn = 0
    P1win = 0
    P2win = 0

    def __int__(self, _db):
        self.db = _db
        self.start()
        self.resetGame()

    def instruction(self):
        print("When it's your turn type the number to represent the location")
        print("   |   |   ")
        print(" 6 | 7 | 8 ")
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(" 3 | 4 | 5 ")
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(" 0 | 1 | 2 ")
        print("   |   |   ")
        print()

    def resetGame(self):
        self.board = [" "] * 10
        self.playersTurn = 0

    def start(self):
        choice = input("X or O").lower()
        if choice == "o":
            self.player1 = "O"
            self.player2 = "X"
        if self.db == True:
            print("self.player1: " + self.player1)
            print("self.player2: " + self.player2)


    def play(self):
        self.start()
        self.instruction()
        if self.db == True:
            self.drawboard()
        gameOver = False
        while gameOver == False:
            self.playersTurn += 1
            if self.db:
                print("Num of Turns: "+ str(self.playersTurn))
            if self.playersTurn %2 ==0:
                currentToken = self.player2
                print("Player2 Turn")
            else:
                currentToken = self.player1
                print("Player1 Turn")


            validChoice = False
            while validChoice == False:
                choice = int(input("Where do you want to make your mark (Choose 0-8)"))
                if choice < 0 or choice > 8:
                    print("You entered an invalid number, only choose a number between 0-8")
                elif self.board[choice] != ' ':
                    print("Choose a different square. This one is already taken")
                else:
                    validChoice = True
                self.board[choice] = currentToken

            if self.db:
                print("self.player: "+ self.player1)

            self.drawboard()
            gameOver = self.bCheckGameOver()

        if self.playersTurn %2 != 0:
            self.P1win += 1
        else:
            self.P2win += 1
        print("Player 1 won " + str(self.P1win) + " times")
        print("Player 2 won " + str(self.P2win) + " times")

    def drawboard(self):
        print("   |   |")
        print(" " + self.board[6] +" | " + self.board[7] + " | " + self.board[8])
        print("   |   |")
        print("-----------")
        print("   |   |")
        print(" " + self.board[3] +" | " + self.board[4] + " | " + self.board[5])
        print("   |   |")
        print("-----------")
        print("   |   |")
        print(" " + self.board[0] +" | " + self.board[1] + " | " + self.board[2])
        print("   |   |")


    def bCheckGameOver(self):
        if self.board[7] != " " and self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            return True
        elif self.board[4] != " " and self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            return True
        elif self.board[1] != " " and  self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            return True
        elif self.board[3] != " " and self.board[6] == self.board[3] and self.board[3] == self.board[0]:
            return True
        elif self.board[4] != " " and self.board[7] == self.board[4] and self.board[4] == self.board[1]:
            return True
        elif self.board[5] != " " and self.board[8] == self.board[5] and self.board[5] == self.board[2]:
            return True
        elif self.board[4] != " " and self.board[6] == self.board[4] and self.board[4] == self.board[2]:
            return True
        elif self.board[4] != " " and self.board[8] == self.board[4] and self.board[4] == self.board[0]:
            return True
        return False


game = TicTacToe()
while True:
    game.play()
    if int(input("Type 1 to play a new game")) ==1:
        game.resetGame()
    else:
        break