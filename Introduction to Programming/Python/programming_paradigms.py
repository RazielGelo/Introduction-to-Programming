# Programming Paradigms

num_list = [1,2,3,4,5,6]

# Procedural Programming
# =============================================
def square_number_list(nums):
    square_list = []
    for num in nums:
        square_list.append(num * num)
    return square_list
        
print(square_number_list(num_list))
# =============================================



# Object-Oriented Programming
# =============================================
class SquareNumbers:
    def __init__(self):
        self.num_squared_list = []
# =============================================



# Functional Programming
# =============================================
def square_num(num):
    return num * num

def square_list(num_list):
    return list(map(square_num, num_list)) 

print(f"{square_list(num_list)} Functional")
# =============================================