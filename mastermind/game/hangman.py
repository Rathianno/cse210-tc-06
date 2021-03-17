class Hangman():
    def __init__(self):
        self._dead = "0"
        self.make_hangman()
    def getState(self):
        return self._hangmanLayers

    def make_hangman(self):
        self._hangmanLayers = []
        self._hangmanLayers.append("  ___ ")
        self._hangmanLayers.append(" /___\\")
        self._hangmanLayers.append(" \\   /")
        self._hangmanLayers.append("  \\ /")
        self._hangmanLayers.append("   "+ self._dead + "\n  /|\\  \n  / \\  \n^^^^^^^")


    #def killOneLayer(self):
        #DOStuff

    def drawHangman(self, lives):
        if lives == 0:
            self._dead = "X"
        self.make_hangman()
        wrong_guess = 4-lives
        for n in range(5-wrong_guess):
            print(self._hangmanLayers[n+wrong_guess])

hangman = Hangman()
hangman.drawHangman(4)