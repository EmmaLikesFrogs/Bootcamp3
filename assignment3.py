# IDC 5100: Introduction to Data Science Bootcamp
# Assingment 3 - Python Basics

## Problem 1 - Create and test a function
"""
To-Do:
Implement a function "mean_min()" that takes in a list of integers and returns a list, with the 
first element being the mean of the input list and the second being the minimum value in the input list.

Note:
You may not use functions from other packages that will do this for you. e.g. np.min(), np.mean(). However,
there are multiple solutions to creating this function.
"""


# Your function here.
ListOfInts = [1, 2, 5, 11, 27]

def mean_min(input_list):
    meanValue = sum(input_list)/len(input_list) 
    minValue = min(input_list)
    return [meanValue, minValue]

result = mean_min(ListOfInts)
print("Mean, Min: ", result)

# Test your function by inputing the list below. Your function should return [8.8, 4].
test_list = [4, 7, 12, 6, 15]

testResult = mean_min(test_list)
print("Test Result", testResult)

## Problem 2 - Create a new class method
"""
To-Do:
Implement a method "price_per_sqft()" that returns the price per square foot of a house object.
"""

class house:
    def __init__(self, price, size, num_bedrooms):
        self.price = price
        self.size = size
        self.num_bedrooms = num_bedrooms

    # Your method here.
    def price_per_sqft(self):
        return self.price / self.size 

# Test your method by creating a house object and calling the method on it.
house_object = house(price = 865000, size = 5200, num_bedrooms = 4)
price_per_sqft_result = round(house_object.price_per_sqft(),2)
print("Price per sqft is: ", price_per_sqft_result)


#publish to github
