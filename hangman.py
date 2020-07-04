from random import*
import time
class hangman:
    gameWon = 0
    wrong = [" "] * 7
    guess = ""
    secret = []
    wronglist = []
    dashlist = []
    #hangman Parts
    head = "O"
    body = "|"
    Larm = "/"
    Rarm = "\ "
    Lleg = "/"
    Rleg = "\ "

    def __int__(self):
        self.difficulty()
        self.hangman()
        self.getWord()
        self.resetGame()


    def play(self):
        self.getWord()
        self.difficulty()
        wrong = 0
        self.dashlist = ["_ "] * len(self.secret)
        gameOver = False
        while gameOver == False:
            self.stickman()
            if self.wrongGuess() == 0:
                self.wronglist.append(self.guess)
                #When wrong guess
                print("Wrong Guess")
                print("")
                print("")
                wrong = wrong +1
                if wrong == 1:
                    self.wrong[1] = self.head
                elif wrong == 2:
                    self.wrong[2] = self.body
                elif wrong == 3:
                    self.wrong[3] = self.Larm
                elif wrong == 4:
                    self.wrong[4] = self.Rarm
                elif wrong == 5:
                    self.wrong[5] = self.Lleg
                elif wrong == 6:
                    self.wrong[6] = self.Rleg
            else:
                #When guess is right
                print("Right Guess!")
                print("")
                print("")
                self.replaceWords()
                if self.dashlist == self.secret:
                    self.gameWon = self.gameWon + 1
                    self.hangman()
                    print(UserName + " guessed the word!")
                    gameOver = True
            #GameOver Code
            if wrong == 6:
                self.hangman()
                print("Game Over :(")
                gameOver = True

    def replaceWords(self):
        count = -1
        for letters in self.secret:
            count = count + 1
            if letters == self.guess:
                self.dashlist[count] = self.guess

    def stickman(self):
        while True:
            print("  _____      ")
            print(" |     |     Word : " + (''.join(self.dashlist)))
            print(" |     "+self.wrong[1] + "     Game Difficulty : " + self.difficulty())
            print(" |    "+self.wrong[3] +self.wrong[2] + self.wrong[4] + "    Game Won : " + str(self.gameWon))
            print(" |    " + self.wrong[5] + " " + self.wrong[6] + "    Wrong Guesses : " + str(''.join(self.wronglist)))
            choice = input("_|_____      Next Guess : ").lower()
            print(" ")
            time.sleep(0.1)
            num = 0
            for letters in self.dashlist:
                if choice == letters:
                    print("You have already chosen this letter")
                    num = 1
            for letters in self.wronglist:
                if choice == letters:
                    print("You have already chosen this letter")
                    num = 1
            if len(choice) != 1:
                print("Enter 1 letter")
            elif choice == "1" or choice == "2" or choice == "3" or \
                            choice == "4" or choice == "5" or choice \
                    == "6" or choice == "7" or choice == "8" or choice == "9":
                print("Enter 1 letter")
            elif num == 0:
                self.guess = choice
                return self.guess



    def hangman(self):
        print("  _____      ")
        print(" |     |     Answer : " + str(''.join(self.secret)))
        print(" |     "+self.wrong[1]+"     Game Difficulty : " + str(self.difficulty()))
        print(" |    "+self.wrong[3] +self.wrong[2] + self.wrong[4] + "    Game Won : " + str(self.gameWon))
        print(" |    " + self.wrong[5] + " " + self.wrong[6] + "    Wrong Guesses : " + str(''.join(self.wronglist)))
        print("_|_____   ")
        print("")

    def getWord(self):
        validWord = False
        while validWord == False:
            #Random words for if user chooses random word
            random = ["people", "chair", "toy", "cat", "electricity", "hangman",
                      "class", "computer", "school", "tissue", "mirror", "tablet", "mattress"
                    , "glasses", "clock", "television", "closet", "table", "water", "phone"]
            WordChoice = int(input("Random Word(Type 1) or User Word(Type 2) "))
            if WordChoice == 1:
                self.secret = random[randint(0, 19)].lower()
                print("Secret word : " + str(self.secret))
            else:
                self.secret = input("Secret word : ").lower()
            self.secret = list(self.secret)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" Scroll up for answer ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            if len(self.secret) < 2:
                print("Enter a longer word")
            else:
                validWord = True

    def difficulty(self):
        if len(self.secret) <5:
            return "Easy"
        elif len(self.secret) > 4 and len(self.secret) < 10:
            return "Normal"
        else:
            return "Hard"

    def wrongGuess(self):
        num = 0
        for letters in self.secret:
            if letters == self.guess:
                num = num + 1
            elif letters != self.guess:
                num = num + 0
        return num

    def resetGame(self):
        self.wrong = [" "] * 7
        self.guess = ""
        self.secret = ""
        self.wronglist = []

game = hangman()
UserName = input("What is your name? ")
print("")
time.sleep(0.4)
print("Hello " + str(UserName))
time.sleep(0.5)
print("Welcome to Hangman")
time.sleep(0.75)
print("")
print("Do you want to use a")

while True:
    game.play()
    print(" ")
    if int(input("New Game(Type 1) or End Game(Type 2) : ")) ==1:
        game.resetGame()
    else:
        print("")
        time.sleep(0.4)
        print(UserName + ", Thanks for playing")
        break