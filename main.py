import palindrome
import transposition
import substitution

str = "this is transposition"
st1 = transposition.scramble2Encrypt(str)
print(str)
print(st1)
print(transposition.scramble2Decrypt(st1))
print()

key = substitution.keyGen()
print("Generated key: " + key)
print("Substitution Cypher of substitutioncypher: ")
str = "substitutioncypher"
st1 = substitution.substitutionEncrypt(str,key)
print(st1)
print("Decryption: " + substitution.substitutionDecrypt(st1, key))
print()

passkey = substitution.genKeyFromPass("hello")
print("Passphrade key:" + passkey)
print("Substitution Cypher with pasphrase key of substitutioncypher: ")
st1 = substitution.substitutionEncrypt(str,passkey)
print(st1)
print("Decryption: " + substitution.substitutionDecrypt(st1, passkey))
print()

str = "this is transposition2"
st1 = transposition.scramble2Encrypt2(str)
print(str)
print(st1)
print(transposition.scramble2Decrypt2(st1))
print()

print("Palindrome Function Testing:")
print("Testing amanaplanacanalpanama: ",palindrome.palindromCheck("amanaplanacanalpanama"))
