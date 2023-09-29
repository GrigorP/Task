from random import choice

class harry_potter:
    def __init__(self, first: str, second: str, third: str, Lord_Voldermord):
        self.all = [first.lower(), second.lower(), third.lower()]
        self.Lord_Voldermord = Lord_Voldermord

    def winner(self):
        my_balls = 0
        for i in range(len(self.Lord_Voldermord)):
            if self.all[0] == choice(self.Lord_Voldermord):
                my_balls += 1
                if my_balls == 2:
                    print("You win")
            else:
                my_balls -= 1

            if self.all[1] == choice(self.Lord_Voldermord):
                my_balls += 1
                if my_balls == 2:
                    print("You win")
            else:
                my_balls -= 1

            if self.all[2] == choice(self.Lord_Voldermord):
                my_balls += 1
                if my_balls == 2:
                    print("You win")
            else:
                my_balls -= 1
            print(my_balls)
            self.all = [input("Input your magic: ").lower() for _ in range(3)]
            

        if my_balls >= 2:
            print("You win")
        else:
            print("You lose")

magic = harry_potter("Avada Kedavra", "Crucio", "imperio", ["Avada Kedavra", "crucio", "imperio"])

magic.winner()