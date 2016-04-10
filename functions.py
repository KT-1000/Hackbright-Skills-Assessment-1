# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".
def print_hello_world():
    """ Takes no arguments and prints the string "Hello World", returns None.
        >>> print_hello_world()
        'Hello World'
        None
    """
    print "Hello World"
#print_hello_world()


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.
def greet(name):
    """ Takes in string, prints the string "Hi <name>", returns None.
        >>> greet('Katie')
        'Hi Katie'
        None
    """
    print "Hi", name
# print greet('Henry')


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.
def multiply_numbers(num_1, num_2):
    """ Takes two numbers and prints their product. Returns None.
        >>> multiply_numbers(3, 2)
        6
        None
        Numbers can be integers or float. Using a float will cause the product
        to be a float.
        >>> multiply_numbers(2.5, 2)
        5.0
        None
    """
    print num_1 * num_2
#print multiply_numbers(2.5, 2)


# 4. Write a function that takes a string and an integer and
#    prints the string that many times
def repeat_string(input_str, repeat_int):
    """Repeats a string a specified number of times.
        Take in a string, and an integer denoting how many times to repeat string.
        >>> repeat_string("hello", 3)
        'hellohellohello'
        None
        Floats will be converted to integers, rounding accordingly.
       >>>repeat_string("hufflepuff", 2.5)
       'hufflepuffhufflepuff'
    """
    print input_str * int(repeat_int)
#print repeat_string("hello", 5)


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".
def relation_to_zero(number):
    """ Takes an integer and prints its relationship to zero: higher, lower or
        zero itself. Returns None. Float will be rounded to integer.
        >>> relation_to_zero(8)
        'Higher than 0'
        None
        >>>relation_to_zero(-155)
        'Lower than 0'
        None
        >>>relation_to_zero(0)
        'Zero'
        None
    """
    number = int(number)
    if number > 0:
        print "Higher than 0"
    elif number < 0:
        print "Lower than 0"
    else:
        print "Zero"

#print relation_to_zero(0.121143234)


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.
def divisible_by_3(number):
    """Takes a number (floats will be converted to integers) and returns True
        if number is divisible by three and False if it is not.
        >>> divisible_by_3(9)
        True
        >>> divisible_by_3(-14)
        False
        >>>divisible_by_3(3.777777)
        True
    """
    number = int(number)
    if number % 3 == 0:
        return True
    elif number % 3 != 0:
        return False
    else:
        print "That wasn't even a number!"

#print divisible_by_3(3.56469191)


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def get_number_of_spaces(sentence_str):
    """Takes a string and returns the number of spaces in that string.
        >>>get_number_of_spaces("The quick brown fox jumps over the lazy dog.")
        8
    """
    # start count of spaces at zero
    total_spaces = 0
    for character in sentence_str:
        # it's a space, so we want to add it to the total
        if character == " ":
            total_spaces += 1
    return total_spaces

#print get_number_of_spaces("5 6 082394 yyyy 7 ")


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.
def get_payment_total(meal_price, tip_percentage=15):
    """Takes a meal price and tip percentage to calculate total price, and returns
        the total meal price including tip.
        >>>get_payment_total(36.98, 20)

    """
    # if a tip percentage order other than the default 15% was entered
    if tip_percentage != 15:
        # convert to decimal so multiplication works appropriately
        tip_percentage = tip_percentage * 0.01
        # to get the full price of a meal,
        # add the meal price before tip
        # to the price of the tip
        meal_price = meal_price + (meal_price * tip_percentage)
    else:
        # 15% is the default
        meal_price = meal_price * 1.15

    return '{:0,.2f}'.format(meal_price)

print get_payment_total(36.98)

# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.
# REQUIRED FOR DOCTESTS
# if __name__ == "__main__":
#     import doctest
#     print
#     result = doctest.testmod()
#     if not result.failed:
#         print "ALL TESTS PASSED. GOOD WORK!"
#     print
#     