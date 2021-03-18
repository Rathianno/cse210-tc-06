class console():

    def display_current_guesses(self,  player, player_guess, hint):
        print("Player" + player + ": " + str(player_guess) + "," + hint)
    
    def get_player_guess(self, player):
        print(player + "'s turn: ")
        guessdoesntwork = True
            while guessdoesntwork:
                guess = input("What is your guess? ")
                try:
                    guess = int(guess)
                except ValueError:
                    print("Make sure you type a number")
                    continue

                if(guess < 0 or guess > 9999):
                    print("Type a number between 0 and 9999")
                    continue
                guessdoesntwork = False
        return result