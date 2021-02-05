# Tests whether the provided string (input) is a palindrome. The function uses a negative index (-1) to determine the
# last character of the string and begins evaluating if the provided string (input) is a palindrome. The function
# returns True if input is a palindrome and False if input is not a palindrome.
# parameters: input: string that is tested if (not) a palindrome
# return: Boolean
#       False: if input is not a palindrome; True: if input is #palindrome

def palindromCheck(input):
    j = -1
    i = 0
    while i < abs(len(input) + j):
        if not input[i].isalpha():
            i += 1
        if not input[j].isalpha():
            j -= 1
        if input[i] != input[j]:
            return False
        j -= 1
        i += 1
    return True
