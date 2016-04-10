"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def print_list(my_list):
    """Print each item in the input list

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9

    """
    for item in my_list:
        print item


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    # if a number is not evenly divisible by two, it's an odd number
    number_list = [number for number in number_list if number % 2 != 0]
    return number_list


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    # if a number is evenly divisible by two, it's an even number
    number_list = [number for number in number_list if number % 2 == 0]
    return number_list


def every_other_item(my_list):
    """Return a list that contains every other item in my_list starting
       with the first item.

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["you", "friend", "are", "very", "good", " ", "at", " ", "coding"])
       ['you', 'are', 'good', 'at', 'coding']
    """
    # stepping by 2 gives a list every other item in the original
    return my_list[::2]


def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    # index i is the current index,
    # my_list[i] is the list item of that current index
    for i in range(0, len(my_list)):
        print i, my_list[i]


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    # if the length of the word is greater than four, it's a long word so grab it
    word_list = [word for word in word_list if len(word) > 4]
    return word_list


def n_long_words(word_list, n):
    """Return all words in input list that are longer than n characters.

    >>> n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
    ['hello', 'spam', 'spam', 'bacon', 'bacon']

    >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
    ['apples', 'bananas']
    """
    # if the length of a word is greater than n, grab it
    word_list = [word for word in word_list if len(word) > n]
    return word_list


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """
    # if the list isn't empty
    if len(number_list) > 0:
        # so we can compare the first int to itself
        # technically the first element in the list is the smallest_int
        # at this point in time (because we haven't looked at anything else)
        smallest_int = number_list[0]
        # compare each number in the number_list to the current smallest_int
        # if it's less than or equal to the current smallest_int
        # rebind smallest_int to the number
        for num in number_list:
            if num <= smallest_int:
                smallest_int = num
            else:
                continue
        return smallest_int
    # the length of the list is zero, so there's nothing to compare
    else:
        return None


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    # if the list isn't empty
    if len(number_list) > 0:
        # so we can compare the first int to itself
        # technically the first element in the list is the largest_int
        # at this point in time (because we haven't looked at anything else)
        largest_int = number_list[0]
        # compare each number in the number_list to the current largest_int
        # if it's less than or equal to the current largest_int
        # rebind largest_int to the number
        for num in number_list:
            if num >= largest_int:
                largest_int = num
            else:
                continue
        return largest_int
    # the length of the list is zero, so there's nothing to compare
    else:
        return None


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    number_list = [(number / 2.0) for number in number_list]
    return number_list


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    word_list = [len(word) for word in word_list]
    return word_list


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    if len(number_list) > 0:
        # start at zero because a number plus zero is the number
        total_sum = 0
        for num in number_list:
            # just add each number to the running total
            total_sum += num
        return total_sum
    else:
        return 0


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    # make sure there are numbers in the num_list
    if len(number_list) > 0:
        # 1 times a number is the number
        total_product = 1
        for num in number_list:
            # multiply the running total by the number
            total_product *= num
        return total_product
    else:
        return 1


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    # make sure there are words in word_list
    if len(word_list) > 0:
        # create an empty string because the joined words will be one (kinda long) string
        join_str = ''
        for string in word_list:
            join_str += string
        return join_str
    # no words in the list, so return an empty string
    else:
        return ''


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    list_len = len(number_list)
    # if there are numbers in the list
    if list_len > 0:
        # add up every number in the list to get the total sum
        total_sum = sum_numbers(number_list)
        # average is the total sum divided by the number of items in the list
        # converted to float so the division occurs appropriately
        average = total_sum / float(list_len)
        return average
    # no numbers in the list, no average to find
    else:
        return None


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """
    # the list is empty, just return an empty string
    if len(list_of_words) == 0:
        return ""
    # the list contains a single string, return that string
    elif len(list_of_words) == 1:
        return list_of_words[0]
    # the list contains multiple words, smash them all into one string
    else:
        comma_string = ""
        for word in list_of_words:
            # the last item on the list just needs to be added to the string
            # without a trailing comma and space
            if word is list_of_words[-1]:
                comma_string += word
            # comma_string is rebound to it's previous value
            # concatenated with the current word
            # concatenated with a comma and space
            else:
                comma_string = comma_string + word + ", "
        # the final string of comma separated values from the initial list
        return comma_string


def foods_in_common(foods1, foods2):
    """Using ANY Python data structure presented in the last week, given 2 lists of foods,
    return a set of items that are in common between the two. (Don't include any duplicates
    in the output collection.)
    For example:

    >>> foods_in_common(["cheese", "bagel", "cake"], ["hummus", "beets", "bagel", "lentils"])
    set(['bagel'])

    If there are no foods in common, return an empty set.

    >>> foods_in_common(["lamb", "chili", "cheese"], ["cake", "ice cream"])
    set([])

    """
    # convert each list to a set so we can find their union (ie common items)
    foods1 = set(foods1)
    foods2 = set(foods2)
    # find the union of the two sets and return that set
    return foods1 & foods2


def reverse_list(my_list):
    """Return the inputted list, reversed.

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

    Do not use the python method reverse()/reversed().

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """
    # start with the last item of the list and move back to the beginning
    my_list = my_list[::-1]

    return my_list


def reverse_list_in_place(my_list):
    """Return the inputted list reversed--WITHOUT creating a new list.
       This will involve moving the items in my_list to different positions
       in the same list.

       Do not use the python methed reverse()/reversed()

        >>> reverse_list_in_place([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list_in_place(["cookies", "love", "I"])
        ['I', 'love', 'cookies']


    """
    # start with the last item in the list and move back to the beginning
    my_list = my_list[::-1]

    return my_list


def duplicates(my_list):
    """Return a list of words which are duplicated in the input list.
       The returned list should be in ascending order.

       >>> duplicates(["apple", "apple", "banana", "cherry", "banana", "apple"])
       ['apple', 'banana']

       >>> duplicates([1, 2, 2, 4, 4, 4, 7])
       [2, 4]
    """
    # create a new empty list to store all the duplicates
    dupe_list = []
    for item in my_list:
        # items are duplicates if they're in the list count more than once
        if my_list.count(item) > 1:
            # only get unique duplicates. Skip it if it's alread in the new list
            if item not in dupe_list:
                dupe_list.append(item)
    return dupe_list


def find_letter_indices(list_of_words, letter):
    """Given a list of words and a letter, return a list of integers that correspond
    to the index of the first occurance of the letter in that word.

    Do not use the .index() list method.

    >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
    [0, 1, 2]

    If the letter doesn't occur in one of the words, use None for that word in
    the output list. For example:

    >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
    [0, 1, 2, None]

    """
    # create a new empty list to hold the letter indices
    letter_indices = []
    # gets us into each word in the list
    for word in list_of_words:
        # get the index of each letter in the word
        for i in range(len(word)):
            # if the word at index i matches the letter
            if word[i] == letter:
                # add only the index to the end of the letter indices list
                letter_indices.append(i)
                # stop after the first occurance of letter in word
                break
            # if the index is the last, the letter doesn't occur in this word
            # so return None
            elif i == len(word) - 1:
                letter_indices.append(None)

    return letter_indices


def largest_n_items(input_list, n):
    """Given a list of integers along with an integer n, return a
    list of the largest n numbers in the input list in ascending order.

    You can assume that n will be less than the length of the list.

    For example:

    >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [59, 700, 6006]

    """
    # make a sorted copy of the initial list so it's lowest to highest
    # go to the -n index (so n from the end) and bind input list to the
    # slice of the list from that index to the end
    input_list = sorted(input_list)[-n:]

    return input_list


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
