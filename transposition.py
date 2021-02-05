def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText


def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText


def scramble2Encrypt2(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch  # if there is no remainder then it is an even character
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1  # increment charCount
    cipherText = evenChars + oddChars  # generate ciphertext by adding even characters before odd characters (opposite than scramble2Encrypt)
    return cipherText


def scramble2Decrypt2(cipherText):
    halfLength = len(cipherText) // 2  # takes half length of the ciphertext
    evenChars = cipherText[:halfLength]  # Find even characters by slicing ciphertext from 0 to halfLength - 1
    oddChars = cipherText[halfLength:]  # Find odd characters by slicing halfLength until the end of the string
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]  # Begin recovering plaintext by taking even characters first
        plainText = plainText + oddChars[i]   # Odd characters

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]  # Prints plaintext + last even character

    return plainText
