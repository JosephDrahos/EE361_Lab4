
def palindromCheck(input):
    for i in range(int(len(input)/2)):
        if input[i] != input[-i-1]:
            return False
    return True