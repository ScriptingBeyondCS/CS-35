#
# hw0pr1.py
#

# An example function

def plus1( N ):
    """ returns a number one larger than its input """
    return N+1


# An example loop (just with a printed countdown)

import time

def countdown( N ):
    """ counts downward from N to 0 printing only """
    for i in range(N,-1,-1):
        print("i ==", i)
        time.sleep(0.01)

    return    # no return value here!


# ++ Challenges:  create and test as many of these five functions as you can.
#
# The final three will be especially helpful!
#
# times42( s ):      which should print the string s 42 times (on separate lines)
# alien( N ):          should return the string "aliii...iiien" with exactly N "i"s
# count_digits( s ):    returns the number of digits in the input string s
# clean_digits( s ):    returns only the digits in the input string s
# clean_word( s ):    returns an all-lowercase, all-letter version of the input string s

