def removeChar(string, idx):
    return string[:idx] + string[idx + 1:]


def keyGen():
    import random
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    key = ""
    for i in range(len(alphabet) - 1, -1, -1):
        idx = random.randint(0, i)
        key = key + alphabet[idx]
        alphabet = removeChar(alphabet, idx)
    return key


def removeDupes(myString):
    newStr = ""
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr


def removeMatches(myString, removeString):
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr


def genKeyFromPass(password):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    password = password.lower()
    password = removeDupes(password)
    lastChar = password[-1]
    lastIdx = alphabet.find(lastChar)
    afterString = removeMatches(alphabet[lastIdx + 1:], password)
    beforeString = removeMatches(alphabet[:lastIdx], password)
    key = password + afterString + beforeString
    return key


def substitutionEncrypt(plainText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText


def substitutionDecrypt(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    cipherText = cipherText.lower()
    plainText = ""
    for ch in cipherText:
        idx = key.find(ch)
        plainText = plainText + alphabet[idx]
    return plainText
