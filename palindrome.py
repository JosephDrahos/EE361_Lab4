# Tests whether the provided string (input) is a palindrome. The function uses a negative index (-1) to determine the
# last character of the string and begins evaluating if the provided string (input) is a palindrome. The function
# returns True if input is a palindrome and False if input is not a palindrome.
# parameters: input: string that is tested if (not) a palindrome
# return: Boolean
#       False: if input is not a palindrome; True: if input is #palindrome

def palindromCheck(input):
    for i in range(int(len(input) / 2)):
        if input[i] != input[-i - 1]:
            return False
    return True
