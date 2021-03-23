import random

class Puzzle:

    def __init__(self):
        self.answer=''
        self.hint=''

    def make_answer(self):
        self.answer=str(random.randint(0000,9999))

    def give_hint(self, guess):
        new_hint=[]

        for i, chr in enumerate(guess):
            
            if chr==self.answer[i]:
                print(i, chr,'true')
                new_hint.append('x')

            elif chr in self.answer:
                print(i,chr,'elifS')
                new_hint.append('o')

            else:
                print(i,chr,'error')
                new_hint.append('*')

        print(new_hint[0], new_hint[1], new_hint[2], new_hint[3], sep='')



    def find_index(self, new_guess, answer):
        return [i for i, ltr in enumerate(answer) if ltr == new_guess]


def main():
    puzz=Puzzle()
    puzz.make_answer()
    puzz.give_hint('0033')
    print(puzz.answer)

main()