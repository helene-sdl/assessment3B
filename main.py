"""
Blackjack
"""


# Provide your solution here
def blackjack(num1: int, num2: int, num3: int):
    sum1 = sum((num1, num2, num3))
    sum2 = sum1 - 10
    if sum1 <= 21:
        return sum1
    elif sum1 > 21 and num1 and num2 and num3 != 11:
        return 'BUST'
    elif sum2 > 21:
        return 'BUST'
    else:
        return sum2



"""
Even Numbers
"""


# Provide your solution here
def even_positive_numbers(list1):
    even_positives = [num for num in list1 if num >= 0 and num % 2 == 0]
    return even_positives


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

print(blackjack(9, 9, 9))
print(blackjack(2, 8, 11))
print(blackjack(3, 8, 11))
print(blackjack(11, 11, 11))
print((blackjack(2, 8, 11)))

print(even_positive_numbers([1, 2, 3]))
print(even_positive_numbers([10, 22, 31, 24, 35, 36]))
print(even_positive_numbers([-10, -22, 31, 24, 35, 36]))


