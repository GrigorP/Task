import math

class name_in_nums:
    def __init__(self, name, nums: dict):
        self.name = name
        self.nums = nums
    
    def name_in_num(self):
        items =  dict(self.nums.items())
        # keys = []
        # values = []
        name_in_numbers = 0 
        for i in self.name:
            for key, value in self.nums.items():
                if i in value:
                    name_in_numbers += key
                    
        if math.sqrt(name_in_numbers) < 5:
            return name_in_numbers, "Yes"
        else:
            return name_in_numbers, "No"

name_num_dict = {
    1 : ["a", "j", "s"],
    2 : ["b", "k", "t"], 
    3 : ["c", "l", "u"], 
    4 : ["d", "m", "v"], 
    5 : ["e", "n", "w"], 
    6 : ["f", "o", "x"],
    7 : ["g", "p", "y"],
    8 : ["h", "q", "z"], 
    9 : ["i", "r"]
}

new_name =  name_in_nums("Grigor".lower(), name_num_dict)

print(new_name.name_in_num())      

