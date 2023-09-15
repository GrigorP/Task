import math

class Temperature:
    def __init__(self, temerature):
        self.temperature = math.ceil(temerature * math.pi)
        
    def COVID_19_test(self):
        if 120 <= self.temperature <= 128:
            print("You Have coronavirus")
        else:
            print("Everything is ok")
    



temp = Temperature(temerature=float(input("Input here your temperature: ")))

temp.COVID_19_test()

    



